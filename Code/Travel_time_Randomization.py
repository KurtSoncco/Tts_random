# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:26:23 2023

@author: kurt-
"""

# Let's begin

from scipy.stats import norm
import numpy as np
import random
from scipy.interpolate import interp1d
import pandas as pd


    
def tts_Rand_Halfspace(zh_mean, Sigmaln_zh, Vh_mean, Sigmaln_Vh, correlation_h, Nprofiles):
    """
    This function generates N realizations of standard normal scores for halfspace depth and Vs.
    
    Parameters:
    zh_mean: Mean of halfspace depth.
    Sigmaln_zh: Logarithmic standard deviation of zh.
    Vh_mean: Mean of halfspace Vs.
    Sigmaln_Vh: Logarithmic standard deviation of Vh.
    correlation_h: Correlation between halfspace depth and Vs.
    Nprofiles: Number of profiles.
    
    Returns:
    z_halfspace: N realizations of halfspace depths.
    SVh: N realizations of halfspace Vs.
    """
    # Generate N realizations of standard normal scores for halfspace depth
    # rand generates a number between [0,1], which could be considered as
    # sampling from normal CDF
    # norminv returns the inverse CDF
    Szh = norm.ppf(np.random.random([Nprofiles]))
    
    # Convert the z-scores to halfspace depths based on halfspace distribution
    # mean/median, standard deviation, and the randomized z-scores
    # then convert from lognormal units to real units
    z_halfspace = np.exp(Szh*Sigmaln_zh + np.log(zh_mean))
    
    # Equation 10 Passeri et al. (2020)
    # Generate N realizations of standard normal scores for halfspace Vs
    # Passeri assumed a bivariate distribution for halfspace depth and Vs
    # Therefore, halfspace Vs z-scores are correlated to halfspace depth
    # z-scores, with correlation_h being this correlation
    SVh = correlation_h*Szh + norm.ppf(np.random.random([Nprofiles]))*np.sqrt(1-correlation_h**2)

    # Equation 11 Passeri et al. (2020)
    # Convert the z-scores to halfspace Vs based on halfspace distribution
    # mean/median, standard deviation, and the randomized z-scores
    # then convert from lognormal units to real units
    Vs_halfspace = np.exp(SVh*Sigmaln_Vh + np.log(Vh_mean))
    
    return z_halfspace, Vs_halfspace


def tts_Rand_Layers(c3, c1, c2, minRate, maxRate, zh_mean, Sigmaln_zh, Nprofiles):
    # Initialize variables for speed
    # these are defined as cell arrays because number of layers might be
    # different for different column models (that's why, we can't save them in
    # a 2D matrix, because each column will have different number of rows)
    depth_all = dict() # includes depth vectors of randomized profiles; depth to top of layers
    rate_all = dict() # includes rate vectors of randomized profiles; rate to mid-depth of layers
    
    # Loop to generate N realization of column models (each column model has
    # multiple layers)
    
    for realization in range(Nprofiles):
    
        # pre-define variables
        H_homo = np.empty(0); # layer boundaries based on homogeneous Poisson process
        rate_realization = np.empty(0); # randomized rate profile for this model
        u = 0; # Cumulative depth from unit exponential distribution
        depth_realization = np.zeros(1); # randomized depth profile for this model (first value is 0, surface)
        
        # keep adding layers until a certain depth is reached
        while True:
            # Generate layer boundaries based on homogeneous Poisson process
            H_homo= np.append(H_homo,-np.log(1-random.random()))    # Layer thickness using unit exponential distribution
            u = np.sum(H_homo)                               # Depth from unit exponential distribution
            
            # Transform to non-homogeneous Poisson process
            ICRF = ( -c2*u/c3 + u/c3 + c1**(-c2+1) )**( 1/(-c2+1) ) - c1   # Inverse cumulative rate function (Eq. 3.10)
            depth_realization = np.append(depth_realization, ICRF)                                      # Depth
            mid_depth = np.mean(depth_realization[-2:]);       # Depth to center of layer
            
            # Get experimental occurrence rate for this layer and compare to
            # acceptable range
            rate = 1/(depth_realization[-1]-depth_realization[-2]);                         # rate is 1/thickness
            min_rate = minRate * (c3 * ( mid_depth + c1 ) ** (-c2));
            max_rate = maxRate * (c3 * ( mid_depth + c1 ) ** (-c2));
            if (rate < min_rate) | (rate > max_rate):  # if layer is outside acceptable bounds
                depth_realization = depth_realization[:-1];            # Remove it
                H_homo = H_homo[:-1];
            else: # if the rate is within limits, append it to the ouput rate_profile
                rate_realization = np.append(rate_realization,rate);
            
            # Stop when last layer is more than 3 standard deviations from depth
            # to halfspace model (i.e., randomized profile is deep enough)
            if depth_realization[-1] > np.exp(np.log(zh_mean) + 3*Sigmaln_zh):   
                # Last layer is more than 3 standard deviations away. 
                
                # Append simulated profile
                depth_all[realization] = depth_realization;
                rate_all[realization] = rate_realization;
        
                # Break loop
                break
            #else
                # Last layer is not more than 3 standard deviations away. Add more
                # layers.
    
    return depth_all, rate_all




def tts_Rand_Merging(depth_all, z_halfspace):
    
    # Create output format
    merged_depths = dict()
    
    # Loop through z_halfspace (i.e., each realization of the N randomized profiles)
    for n in range(z_halfspace.size):
        
        # create an array that saves the squared difference between a
        # randomized halfspace depth and layer depths of each remaining column 
        # model
        diff = []
        
        # create an array that saves the number of the layer interface that is
        # optimal for the bedrock depth
        min_idx = []
        
        # Loop through remaining column models (after excluding those merged
        # already)
        for i in range(len(depth_all)):
            # get the difference between the halfspace's depth and each layer
            # interface in this column model. Only save the minimum difference,
            # which would be the optimal layer interface for this column model.
            # This will not necessarily be the last layer interface, because
            # column models are generated to be deeper than halfspace.
            diff.append(np.min(np.power(z_halfspace[n] - depth_all[i],2)))
            min_idx.append(np.argmin(np.power(z_halfspace[n] - depth_all[i],2)))
        
        
        # Get the most optimal column model for this halfspace model
        indx = np.argmin(diff)
        
        # Save optimal column model from surface to optimal interface
        merged_depths[n] = depth_all[indx][:min_idx[indx]+1];
        
        # Force halfspace depth on last layer
        merged_depths[n][-1] = z_halfspace[n];
        
        # Remove merged column
        depth_all[indx] = np.empty(0);
        new_dict = dict()
        k = 0
        for _, v in depth_all.items():
            if v.size != 0:
                new_dict[k] = v
                k +=1
                
        depth_all = new_dict
    
    return merged_depths



def tts_Rand_PostMerging(merged_depths, c3, c1, c2, minRate, maxRate, zh_mean, Sigmaln_zh):
    
    
    # Create output format
    final_merged_depths = merged_depths;
    
    # Get N, original number of simulated profiles.
    N  = len(merged_depths);
    
    # keep track of halfspace depths that were unsuccessfully merged
    Rejected_z_halfspace = np.empty(0);
    
    # loop through merged column models
    for n in range(len(merged_depths)):
    
        # get mid_depth to each layer
        mid_depth = np.convolve(merged_depths[n],np.ones(2,dtype=int),'valid')/2;
    
        # get rate of each layer (1/thickness)
        temp_rate = 1/np.diff(merged_depths[n]);
    
        # get rate parameter at mid depth of last layer for this profile
        ratez = c3*(mid_depth[-1]+c1)**(-c2);
    
        # check if rate of last layer is acceptable
        if (minRate*ratez > temp_rate[-1]) and (temp_rate[-1] > maxRate*ratez):
    
            # if not acceptable, save the bedrock that was unsuccessfully
            # merged to re-simulate columns and re-merge
            Rejected_z_halfspace = np.append(Rejected_z_halfspace, merged_depths[n][-1]);
            
            # remove layers of unacceptable column
            final_merged_depths[n] = [];
    
    while len(Rejected_z_halfspace) != 0:
        # indices of models that were removed in step above
        rejected_models = [k for k,v in final_merged_depths.items() if len(v) == 0]
            
        # else, resimulate N column models and re-merge
        # Generate layering
        resimulated_depths, _ = tts_Rand_Layers(c3, c1, c2, minRate, maxRate, zh_mean, Sigmaln_zh, N)
    
        # re-merge
        merged_depths = tts_Rand_Merging(resimulated_depths, Rejected_z_halfspace)
        
        # reset halfspace depths that were unsuccessfully merged
        Rejected_z_halfspace = [];
        
        for n in range(len(rejected_models)):
    
            # get mid_depth to each layer
            mid_depth = np.convolve(merged_depths[n],np.ones(2,dtype=int),'valid')/2;
    
            # get rate of each layer (1/thickness)
            temp_rate = 1/np.diff(merged_depths[n]);
    
            # get rate parameter at mid depth of last layer for this profile
            ratez = c3*(mid_depth[-1]+c1)**(-c2);
    
            # check if rate of last layer is acceptable
            if (minRate*ratez > temp_rate[-1]) and (temp_rate[-1] > maxRate*ratez):
                
                # if acceptbale, append
                final_merged_depths[rejected_models[n]] = merged_depths[n];
                
            else:
                # if not acceptable, save the halfspace that was unsuccessfully
                # merged to re-simulate columns and re-merge
                Rejected_z_halfspace = np.append(Rejected_z_halfspace, merged_depths[n][-1]);
     
    
    
    return final_merged_depths



def tts_Rand_Vs(depth_all, base_depth, base_Vs, corr_model, sigmalntts, Vs_halfspace, delta_corr):
    
    # Correlation parameters (see Table 3.3 in Kottke and Rathje 2009)
    if corr_model == 'GeoMatrix_A&B':      # Rock and shallow soil
        rho_0 = 0.96;   rho_200 = 0.96; 
        delta = 10.00;  d_0 = 0.0;
        b = 0.095;
    elif corr_model == 'GeoMatrix_C&D':  # Deep narrow/broad soil
        rho_0 = 0.99;   rho_200 = 1.00; 
        delta = 8.00;   d_0 = 0.0;
        b = 0.160;
    elif corr_model == 'USGS_A&B':       # Vs30 > 360 m/s
        rho_0 = 0.95;   rho_200 = 1.00; 
        delta = 4.20;   d_0 = 0.0;
        b = 0.138;
    elif corr_model == 'USGS_C&D':       # Vs30 < 360 m/s
        rho_0 = 0.99;   rho_200 = 1.00; 
        delta = 3.90;   d_0 = 0.0;
        b = 0.293;  
    elif corr_model == 'USGS_A':         # Vs30 > 760 m/s
        rho_0 = 0.95;   rho_200 = 0.42; 
        delta = 3.40;   d_0 = 0.0;
        b = 0.063;
    elif corr_model == 'USGS_B':         # 360 < Vs30 < 760 m/s
        rho_0 = 0.97;   rho_200 = 1.00; 
        delta = 3.80;   d_0 = 0.0;
        b = 0.293;   
    elif corr_model == 'USGS_C':         # 180 < Vs30 < 360 m/s
        rho_0 = 0.99;   rho_200 = 0.98; 
        delta = 3.90;   d_0 = 0.0;
        b = 0.344;    
    elif corr_model == 'USGS_D':         # Vs30 < 180 m/s
        rho_0 = 0.00;   rho_200 = 0.50; 
        delta = 5.00;   d_0 = 0.0;
        b = 0.744;    
    else:         # Custom correlation parameters
        if not(len(corr_model)==5):
            raise Exception('Invalid number of custom correlation parameters')
        elif isinstance(corr_model,str):
            raise Exception('Invalid correlation model')

        rho_0, rho_200, delta, d_0, b = corr_model


    # Initialize variables for speed
    # these are defined as cell arrays because number of layers might be
    # different for different column models (that's why, we can't save them in
    # a 2D matrix, because each column will have different number of rows)
    Vs_all = dict();
    tts_all = dict();
    
    # loop over each randomized profile
    for n in range(len(Vs_halfspace)):
        
        # depth of randomized profile we are iterating on 
        depth = depth_all[n];
        
        # Calculate mid-depth of each layer and distance between successive 
        # mid-depths for profile excluding halfspace
        
        # initialize variables
        t = np.zeros(depth.size-1); # distance between midpoint depths
        H = np.zeros(depth.size-1); # thickness of layers
        d_mid = np.zeros(depth.size-1);
        
        # loop through each layer up to the layer directly above halfspace
        for k in range(len(depth)-1):
            H[k] = depth[k+1] - depth[k]; # thickness of a layer is simply different of the depths
            d_mid[k] = depth[k]+H[k]/2; # mid-depth is the depth to a layer + half its thickness
            if k == 0: # first layer
                t[k] = 0; # not needed for first layer, above it is ground surface
            else:
                t[k] = d_mid[k]-d_mid[k-1]; # difference in successive mid-depths
    
        # Initialize variables for speed
        Z = np.zeros_like(d_mid); # standard z scores for tts for each randomized layer
        rho_d = np.zeros_like(d_mid); # depth-dependent correlation
        rho_t = np.zeros_like(d_mid); # thickness-dependent correlation
        rho = np.zeros_like(d_mid); # total correlation
        mediantts = np.zeros_like(depth); # base-case tts profile
    
        # Calculate correlation coefficients for each layer
        Z[0] = np.random.normal(0,1);         # Standard normal variable of top layer                 
        rho[0] = 1;                  # Correlation associated with first layer
        for k in range(1,len(d_mid)):
            rho_t[k] = rho_0 * np.exp(-t[k]/delta);                      # Eq. 4 Hallal et al. (2022)
            if d_mid[k] > 200:
                rho_d[k] = rho_200;                                     # Eq. 3 Hallal et al. (2022)
            else:
                rho_d[k] = rho_200 * ((d_mid[k]+d_0)/(200+d_0))**b;  # Eq. 4 Hallal et al. (2022)
    
            rho[k] = np.min([(1-rho_d[k])*rho_t[k]+rho_d[k]+delta_corr,1]);  # Eq. 2 Hallal et al. (2022) + fixed constant
    
            Z[k] = rho[k]*Z[k-1] + np.random.normal(0,1)*np.sqrt(1-rho[k]**2);   # Eq. 6 Hallal et al. (2022)
        
    
        # Limit Z to +/- 2 as recommended
        Z[Z < -2] = -2;
        Z[Z > 2] = 2;
    
        # Calculate Base Cumulated Travel time at bottom depth of each layer of the
        # layering realization (based on reference profile)
        # Get base-case tts
        # simply cumulative sum of each layer thickness divided by its Vs
        # add very deep layer below halfspace
        base_tts = np.cumsum(np.diff(np.append(base_depth,1000))/base_Vs);
        # append 0 at depth 0 
        base_tts = np.append(0, base_tts);
        # get base-case tts at mid_depth of the randomized profile using linear interpolation
        mediantts = np.interp(depth, np.append(base_depth,1000), base_tts);
        
        # Base model
        tts_0 = np.interp(base_depth, np.append(base_depth,1000), base_tts);
    
        # first value is zero, remove it
        mediantts = mediantts[1:];
    
        # Compute tts (assuming lognormal distribution)
        tts_all[n] = np.exp( sigmalntts*Z + np.log(mediantts));   
        Vs_all[n] = np.zeros_like(depth);
    
        # Convert tts to Vs
        for i in range(len(depth)-1):
            if i == 0:
                Vs_all[n][i] = (H[i])/tts_all[n][i];
            else:
                Vs_all[n][i] = (H[i])/(tts_all[n][i] - np.sum(H[:i]/Vs_all[n][:i]));
        
        # enforce randomized halfspace Vs on last value
        Vs_all[n][-1] = Vs_halfspace[n];
        
        # Append 0 at depth 0
        tts_all[n] = np.append(0,tts_all[n])
        
        
        
    
    
    
    return Vs_all, tts_all, tts_0




def extrapolate_plot(Vs_all, tts_all, base_tts, Vs, Depth, final_merged_depths, Nprofiles, threshold=0.50):
    
    # Extract the maximum depth
    df = pd.DataFrame.from_dict(final_merged_depths, orient='index').transpose()
    max_depth = np.max(np.max(df))
    
    # Increase by threshold
    new_max = max_depth * (1+threshold)
    
    # New Depth
    new_depth = np.append(Depth, new_max)
    
    # Interpolate all tts and Vs
    f = interp1d(Depth, base_tts, fill_value="extrapolate")
    new_base_tts = f(new_depth)
    new_Vs = np.append(Vs,Vs[-1])
    
    new_tts_all = {}
    new_Vs_all = {}
    new_final_merged_depths = {}
    for n in range(Nprofiles):
        # New depth
        new_depth_all = np.append(final_merged_depths[n],new_max)
        
        f = interp1d(final_merged_depths[n], tts_all[n], fill_value="extrapolate")
        new_tts_all[n] = f(new_depth_all)
        new_Vs_all[n] = np.append(Vs_all[n],Vs_all[n][-1])
        new_final_merged_depths[n] = new_depth_all

    
    
    
    return new_Vs_all, new_tts_all, new_base_tts, new_Vs, new_depth, new_final_merged_depths



def standard_deviation(Vs_all, tts_all, base_tts, base_Vs, base_Depth, depth_all, Nprofiles):
    # This code calculates the standard deviation of Vs and tts across different
    # depths by interpolating at different values of Vs or tts and calculating the 
    # standard deviation of the log normal distribution.
    
    # First, we create a pandas dataframe to compute the max depth
    df = pd.DataFrame.from_dict(depth_all, orient='index').transpose()
    max_depth = np.max(np.max(df))
    
    # Create an array of depth until that max_depth
    depth_inter = np.linspace(0, max_depth,100)
    
    # For tts 
    tts_interp1d = {}

    f = interp1d(base_Depth, base_tts, fill_value="extrapolate")
    base_tts_intp = f(depth_inter)
    tts_interp1d['Base'] = base_tts_intp

    for n in range(Nprofiles):
        f = interp1d(depth_all[n], tts_all[n], fill_value="extrapolate")
        tts_interp1d[n] = f(depth_inter)
        
    df2 = pd.DataFrame.from_dict(tts_interp1d, orient='columns')
    std_tts = np.std(np.log(df2.values),axis=1)
    
    # For Vs
    Vs_interp = {}
    step_fun = interp1d(base_Depth, base_Vs, kind='previous',fill_value="extrapolate")
    Vs_interp['Base'] =  step_fun(depth_inter)


    for n in range(Nprofiles):
        step_fun = interp1d(depth_all[n], Vs_all[n], kind='previous',fill_value="extrapolate")
        Vs_interp[n] = step_fun(depth_inter)

    df3 = pd.DataFrame.from_dict(Vs_interp, orient='columns')
    std_Vs = np.std(np.log(df3.values),axis=1)
    
    # Compute the median
    median_tts = np.median(df2.values[:,1:],axis=1)
    median_Vs = np.median(df3.values[:,1:],axis=1)
    
    return std_tts, std_Vs, depth_inter, median_tts, median_Vs
    
    
    
    



