# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:34:38 2023

@author: kurt-
"""

import numpy as np
import pandas as pd
from Travel_time_Randomization import *
import matplotlib.pyplot as plt


def Travel_time(Vs: list,Depth: list,Nprofiles=50,Sigmaln_zh=0.05,Sigmaln_Vh=0.05,sigmalntts=0.05,c_values=None,fig_plot=True,save_file=True):
    """
    This main function creates the N profiles with travel time randomization.
    
    Parameters:
    Vs (list): Array of shear wave velocities.
    Depth (list): Array containing position of layers.
    Nprofiles (int, optional): Number of profiles. Default is 50.
    Sigmaln_zh (float, optional): Logarithmic standard deviation of zh. Default is 0.05.
    Sigmaln_Vh (float, optional): Logarithmic standard deviation of Vh. Default is 0.05.
    sigmalntts (float, optional): Logarithmic standard deviation of tts. Default is 0.05.
    c_values (list, optional): Coefficients for layer occurrence rate parameter. Default is None.
    fig_plot (bool, optional): If True, the function will plot the results. Default is True.
    save_file (bool, optional): If True, the function will save the results to a file. Default is True.
    
    Returns:
    The function returns the plot of randomized profiles with a provided output function for different programs.
    """
    
    ## Optional Generic Inputs
    # Note that these are "generic", and not "site-specific". Meaning, they
    # were developed by averaging information from many sites. Whenever
    # possible, site-specific input parameters are strongly encouraged.
    # Otherwise, the sensitivity of the results to these input parameters and
    # the associated uncertainty should be considered.
    # Note that these input parameters are based on recommendations by Toro
    # (1995), Passeri et al. (2020), and Hallal et al. (2022).
    # c1, c2, c3 = coefficients for layer occurrence rate parameter (Toro 1995)
    # rho200, d0, b, rho0, and delta = parameters for correlation model (Passeri et al. 2020)
    # correlation_h = correlation coefficient between halfspace depth and Vs (Passeri et al. 2020)
    # delta_corr = fixed correlation to be added to the correlation values (Hallal et al. 2022)
    # sigmalntts = logarithmic standard deviation of tts (Hallal et al. 2022)
    # minRate, maxRate = multipliers to define acceptable range for occurrence rate (Hallal et al. 2022)
    # In addition to the inputs above, the inputs below are also needed. There
    # are no generic values for these inputs. However, some common values can
    # be found in the literature.
    
    
    # Unless specified:
    if c_values == None:
        # Toro traditional model 
        c1 = 10.86;
        c2 = 0.89;
        c3 = 1.98;
        
        
        rho200 = 0.766;
        d0 = 0;
        b = 0.2355;
        rho0 = 0.6364;
        delta = 5.8532;
        
        
        correlation_h = 0.508;
        delta_corr = 0.2;
        minRate = 0.7;
        maxRate = 1.5;
    else:
        c1,c2,c3,rho200,d0,b,rho0,delta,correlation_h,delta_corr,minRate,maxRate = c_values
    
    
    ## Additional Inputs

    #Sigmaln_zh= 0.05; # logarithmic standard deviation of the halfspace depth
    #Sigmaln_Vh = 0.05; # logarithmic standard deviation of the halfspace Vs
    #Nprofiles = 50; # Number of randomized profiles to generate
    
    # Plot Vs profile
    if fig_plot == True:
        # Initiate Figure
        figure, ax1 = plt.subplots(figsize=(4,4));
        #rot = transforms.Affine2D().rotate_deg(90)
        #set(gcf,'units','inches','position',[0.1,4.5,3,3])
    
        # Plot Vs
        # Because of how stairs() works, we will plot depth on x-axis and Vs on
        # y-axis and then flip the view to get correct plot
        ax1.step(Vs,Depth,'-k', lw=1, label='Base-Case Vs',where='pre')
        ax1.invert_yaxis()
        ax1.xaxis.tick_top() 
        ax1.xaxis.set_label_position('top') 
    
        # Label axes
        ax1.set_ylabel('Depth')
        ax1.set_xlabel('Vs')
    
    
    # The format of Depth and Vs assumes that the last value is the starting
    # depth of the halfspace and its Vs. These are assumed to be the
    # mean/median values used to randomize N halfspace depths and their Vs.
    zh_mean = Depth[-1]
    Vh_mean = Vs[-1]
    # Development of the code
    ## Randomize Halfspace Depth and Vs
    z_halfspace, Vs_halfspace = tts_Rand_Halfspace(zh_mean, Sigmaln_zh, Vh_mean, Sigmaln_Vh, correlation_h, Nprofiles);

    if fig_plot == True:
        # Plot Results
        # Initiate Figure
        fig, ax = plt.subplots(1,2)
        fig.suptitle('Randomized Halfspace Depth and Vs')
    
    
        # Subplot 1: Halfspace Depth
        ax[0].hist(z_halfspace,label='Randomized',edgecolor="black")
        ax[0].set_xlabel('Halfspace Depth')
        ax[0].set_ylabel('Count')
        ax[0].vlines(zh_mean,ax[0].get_ylim()[0],ax[0].get_ylim()[1],color='red', lw=1, label='Base-Case')
        ax[0].legend()
    
        # Subplot 2: Halfspace Vs
        ax[1].hist(Vs_halfspace,edgecolor="black")
        ax[1].set_xlabel('Halfspace Vs')
        ax[1].set_ylabel('Count')
        ax[1].vlines(Vh_mean,ax[1].get_ylim()[0],ax[1].get_ylim()[1],color='red', lw=1)
    
        # Add results to Figure 1, Vs profile
        ax1.scatter(Vs_halfspace,z_halfspace, label='Randomized Halfspaces', s=5)
        ax1.scatter(Vh_mean, zh_mean, color='red', s=15, label='Base-Case Halfspace')
        ax1.legend(loc='upper right') # add legend

    ## Randomize Layer Thicknesses
    depth_all, rate_all = tts_Rand_Layers(c3, c1, c2, minRate, maxRate, zh_mean, Sigmaln_zh, Nprofiles);

    ## Merge Randomized Layer Thicknesses with Randomized Halfspace Models

    # Merge first without checking if last layer becomes unacceptable after
    # merging
    merged_depths = tts_Rand_Merging(depth_all, z_halfspace);

    # check last layer and re-merge if needed
    final_merged_depths = tts_Rand_PostMerging(merged_depths, c3, c1, c2, minRate, maxRate, zh_mean, Sigmaln_zh);

    # Plot Results
    if fig_plot == True:
        # This will allow us to visualize the randomized layer thicknesses
        # Initiate Figure
        fig2, ax2 = plt.subplots(figsize=(9.8, 4.5))
    
        #set(gcf,'units','inches','position',[9.8,4.5,6.5,3])
    
        # define 100 colors to plot layer thicknesses. Layers 1 will have same
        # color, layers 2 same color, etc...
        layer_colors = [np.random.choice(range(256), size=3)/255 for i in range(100)];
    
        # loop over realizations
        for realization in range(len(final_merged_depths)):
            
            # loop over layers for each realization
            for layer in range(len(final_merged_depths[realization])-1):
                
                # plot each layer as a colored rectangle with randomized thickness
                x0, y0, w, h = [realization-.5,final_merged_depths[realization][layer],1,final_merged_depths[realization][layer+1]-final_merged_depths[realization][layer]]
                rectangle = plt.Rectangle((x0,y0), w, h, facecolor=layer_colors[layer], edgecolor="black")
                ax2.add_patch(rectangle)
                ax2.axis("scaled")
    
    
        # control appearance
        ax2.invert_yaxis()
        ax2.set_aspect(0.5)
    
        # Label axes
        ax2.set_xlim([0.5,realization+0.5])
        ax2.set_ylabel('Depth')
        ax2.set_xlabel('Realization')
        fig2.suptitle('Randomized Layer Thicknesses After Merging')
    


    ## Randomize tts

    # save inputs for correlation model in required format
    corr_model = [rho0, rho200, delta, d0, b];

    # randomize tts and return Vs
    Vs_all, tts_all, base_tts = tts_Rand_Vs(final_merged_depths, Depth, Vs, corr_model, sigmalntts, Vs_halfspace, delta_corr);


    # Extrapolate to a single depth
    Vs_all, tts_all, base_tts, Vs, Depth, final_merged_depths = extrapolate_plot(Vs_all, tts_all, base_tts, Vs, Depth, final_merged_depths, Nprofiles)

    # Calculate the standard deviation
    std_tts, std_Vs, depth_inter, median_tts, median_Vs = standard_deviation(Vs_all, tts_all, base_tts, Vs, Depth, final_merged_depths, Nprofiles)


    # -------------------------------------------------------------------------
    # Plot final results
    #
    # -------------------------------------------------------------------------
    if fig_plot == True:
        # Plot Vs profile
        # Initiate Figure
        fig3, ax3 = plt.subplots(figsize=(4,4))
        ax3.set_ylabel('Depth')
        ax3.set_xlabel('Vs')
    
        # Plot Randomized Vs
        # plot only 1 for legend
        ax3.step(Vs_all[0], final_merged_depths[0], label='Randomized Vs', \
                 color=[.5,.5,.5],where='pre')
        for realization in range(Nprofiles):
            ax3.step(Vs_all[realization], final_merged_depths[realization], \
                     alpha=0.5, color=[.5,.5,.5],where='pre')
    
    
        # Plot Base-case Vs
        # Because of how stairs() works, we will plot depth on x-axis and Vs on
        # y-axis and then flip the view to get correct plot
        ax3.step(Vs, Depth, '-k', lw=1.2, label='Base-Case Vs', where='pre')
        #view([90 -90])
        ax3.legend(loc='upper right')
        ax3.invert_yaxis()
        ax3.xaxis.tick_top() 
        ax3.xaxis.set_label_position('top') 
        ax3.set_title('Final Randomized Vs Profiles');
        
        
    
    # Additonal plots 
    
    # tts vs Depth
    if fig_plot == True:
        # Plot Vs profile
        # Initiate Figure
        fig4, ax4 = plt.subplots(figsize=(4,4))
        ax4.set_ylabel('Depth')
        ax4.set_xlabel('Travel Time tts')
    
        # Plot Randomized Vs
        # plot only 1 for legend
        ax4.plot(tts_all[0], final_merged_depths[0], label='Randomized tts', \
                 color=[.5,.5,.5])
        for realization in range(Nprofiles):
            ax4.plot(tts_all[realization], final_merged_depths[realization], \
                     alpha=0.5, color=[.5,.5,.5])
    
    
        # Plot Base-case Vs
        # Because of how stairs() works, we will plot depth on x-axis and Vs on
        # y-axis and then flip the view to get correct plot
        ax4.plot(base_tts, Depth, '-k', lw=1.2, label='Base-Case tts')
        #view([90 -90])
        ax4.legend(loc='upper right')
        ax4.invert_yaxis()
        ax4.xaxis.tick_top() 
        ax4.xaxis.set_label_position('top') 
        ax4.set_title('Final Randomized tts Profiles');
        
    
        
    # Plot 4x4 figure
    if fig_plot == True:
        # Plot 4x4 figure
        fig0, ax0 = plt.subplots(2,2,figsize=(10,10))
        
        # Vs plot
        ax0[0,0].set_ylabel('Depth (m)')
        ax0[0,0].set_xlabel('Vs (m/s)')
    
        # Plot Randomized Vs
        # plot only 1 for legend
        ax0[0,0].step(Vs_all[0], final_merged_depths[0], label='Randomized Vs', color=[.5,.5,.5],where='pre')
        for realization in range(Nprofiles):
            ax0[0,0].step(Vs_all[realization], final_merged_depths[realization], alpha=0.5, color=[.5,.5,.5],where='pre')
    
    
        # Plot Base-case Vs
        # Because of how stairs() works, we will plot depth on x-axis and Vs on
        # y-axis and then flip the view to get correct plot
        ax0[0,0].step(Vs, Depth, '-k', lw=1.2, label='Base-Case Vs', where='pre')
        ax0[0,0].step(median_Vs, depth_inter, '--', color='#90EE90', lw=1.0, label='Median', where='pre')
        #view([90 -90])
        ax0[0,0].set_xlim(xmin=0)
        ax0[0,0].set_ylim(ymin=0,ymax=Depth[-1])
        ax0[0,0].legend(loc='upper right')
        ax0[0,0].invert_yaxis()
        ax0[0,0].xaxis.tick_top()
        ax0[0,0].xaxis.set_label_position('top') 
        #ax0[0,0].set_title('Final Randomized Vs Profiles');
        
        
        # std_sigma plot
        ax0[0,1].plot(std_Vs, depth_inter)
        ax0[0,1].set_ylabel('Depth (m)')
        #ax0[0,1].set_xlabel(r'$\sigma_{ln V_s}$')
        ax0[0,1].set_xlim(xmin=0, xmax=0.5)
        ax0[0,1].set_ylim(ymin=0, ymax=Depth[-1])
        ax0[0,1].invert_yaxis()
        ax0[0,1].xaxis.tick_top()
        ax0[0,1].xaxis.set_label_position('top') 
        ax0[0,1].set_title(r'$\sigma_{ln V_s}$');
        
        # tts plot
        ax0[1,0].set_ylabel('Depth (m)')
        ax0[1,0].set_xlabel('Travel Time tts (s)')
    
        # Plot Randomized Vs
        # plot only 1 for legend
        ax0[1,0].plot(tts_all[0], final_merged_depths[0], label='Randomized tts', \
                 color=[.5,.5,.5])
        for realization in range(Nprofiles):
            ax0[1,0].plot(tts_all[realization], final_merged_depths[realization], \
                     alpha=0.5, color=[.5,.5,.5])
    
    
        # Plot Base-case Vs
        # Because of how stairs() works, we will plot depth on x-axis and Vs on
        # y-axis and then flip the view to get correct plot
        ax0[1,0].plot(base_tts, Depth, '-k', lw=1.2, label='Base-Case tts')
        ax0[1,0].plot(median_tts, depth_inter, '--', color='#90EE90', label='Median')
        #view([90 -90])
        ax0[1,0].set_xlim(xmin=0)
        ax0[1,0].set_ylim(ymin=0,ymax=Depth[-1])
        ax0[1,0].legend(loc='upper right')
        ax0[1,0].invert_yaxis()
        ax0[1,0].xaxis.tick_top() 
        ax0[1,0].xaxis.set_label_position('top') 
        #ax0[1,0].set_title('Final Randomized tts Profiles');
        
        
        # Plot std_lntts
        ax0[1,1].plot(std_tts, depth_inter)
        ax0[1,1].vlines(sigmalntts,ymin=0,ymax=Depth[-1],color='red')
        ax0[1,1].text(sigmalntts+0.002, 60.5, 'Input: '+str(sigmalntts), rotation=90, color='red')
        ax0[1,1].set_ylabel('Depth (m)')
        #ax0[0,1].set_xlabel(r'$\sigma_{ln V_s}$')
        ax0[1,1].set_xlim(xmin=0,xmax=0.10)
        ax0[1,1].set_ylim(ymin=0,ymax=Depth[-1])
        ax0[1,1].invert_yaxis()
        ax0[1,1].xaxis.tick_top()
        ax0[1,1].xaxis.set_label_position('top') 
        ax0[1,1].set_title(r'$\sigma_{ln tts}$')
        
        plt.savefig('Code\4x4.png',dpi=300,bbox_inches='tight');
        
    # Save file of Vs
    if save_file == True:
        df1 = pd.DataFrame.from_dict(Vs_all, orient='index').transpose()
        df2 = pd.DataFrame.from_dict(final_merged_depths, orient='index').transpose()
        df = df1.join(df2,rsuffix=" Depth",lsuffix =" Vs")
        
        # sort columns
        idx = np.argsort([k[0:2] for k in df.columns])
        df = df.iloc[:,idx]
        df.to_csv("Data.csv")
        

    return Vs_all, final_merged_depths, tts_all, base_tts
