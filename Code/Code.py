# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:34:38 2023

@author: kurt-
"""

import numpy as np
import pandas as pd
from Travel_time_Randomization import *
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os



def Travel_time(Vs: list, Depth: list, Nprofiles=50, Sigmaln_zh=0.05, Sigmaln_Vh=0.05, sigmalntts=0.05,
                c_values_Toro=None, half_space_Toro=None, interlayer_c=None, delta_rho=None,
                fig_plot=True, save_file=True, filename="", show_fig=False):
    """
    This main function creates the N profiles with travel time randomization.
    
    Parameters:
    Vs (list): A list of shear wave velocities for each layer.
    Depth (list): A list of depths corresponding to the bottom of each layer.
    Nprofiles (int, optional): The number of seismic profiles to generate. Default is 50.
    Sigmaln_zh (float, optional): The logarithmic standard deviation of the layer thickness. Default is 0.05.
    Sigmaln_Vh (float, optional): The logarithmic standard deviation of the shear wave velocity. Default is 0.05.
    sigmalntts (float, optional): The logarithmic standard deviation of the travel time. Default is 0.05.
    c_values_Toro (list, optional): A list of coefficients for the layer occurrence rate parameter. If None, Pasari's original parameters are used.
    half_space_Toro (list, optional): A list of parameters for generating the depth of the half-space. If None, Pasari's original parameters are used.
    interlayer_c (list, optional): A list of parameters for generating the interlayer correlation. If None, Pasari's original parameters are used.
    delta_rho (float, optional): A fixed value for the correlation parameter to avoid unrealistic shear wave velocities. If None, a fixed value of 0.2 is used.
    fig_plot (bool, optional): If True, a plot of the generated profiles is created. Default is True.
    save_file (bool, optional): If True, the generated profiles are saved to a file. Default is True.
    filename (str, optional): The name of the file to save the profiles to. If empty, a default name is used.
    show_fig (bool, optional): If True, the plot of the generated profiles is displayed. Default is False.

    Returns:
    A list of generated seismic profiles.
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
    if c_values_Toro == None:
        # Toro traditional model 
        c1 = 10.86;
        c2 = 0.89;
        c3 = 1.98;

        # Toro's limit for interface rate
        minRate = 0.5;
        maxRate = 1.5;
    else:
        c1,c2,c3,minRate,maxRate = c_values_Toro

    if interlayer_c == None:
        # Parameters for interlayer correlation, for generic case
        rho200 = 0.766;
        d0 = 0;
        b = 0.2355;
        rho0 = 0.6364;
        delta = 5.8532;
    else:
        rho200,d0,b,rho0,delta = interlayer_c

    if half_space_Toro == None:
        # Parameter for halspace velocity randomization        
        correlation_h = 0.508;
    else: 
        rho200,d0,b,rho0,delta,correlation_h = half_space_Toro

    if delta_rho == None:
        # Fixed value for correlation parameter to avoid unrealistic Vs values
        delta_corr = 0.2;
    else:
        delta_corr = delta_rho
    
    # Plot Vs profile
    if fig_plot == True:

        # Create folder to save figures
        if not os.path.exists('Figures'):
            os.makedirs('Figures')

        # Add path to filename
        filename = 'Figures/' + filename
        
        # Figure name
        fig_name = filename + " Vs_profile.png"
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


    # -------------------------------------------------------------------------
    
    
    # The format of Depth and Vs assumes that the last value is the starting
    # depth of the halfspace and its Vs. These are assumed to be the
    # mean/median values used to randomize N halfspace depths and their Vs.
    zh_mean = Depth[-1]
    Vh_mean = Vs[-1]
    # Development of the code
    ## Randomize Halfspace Depth and Vs
    z_halfspace, Vs_halfspace = tts_Rand_Halfspace(zh_mean, Sigmaln_zh, Vh_mean, Sigmaln_Vh, correlation_h, Nprofiles);

    if fig_plot == True:
        # Figure name
        fig_name = filename + " Halfspace.png"
        # Initiate Figure
        fig, ax = plt.subplots(1,2,figsize=(12, 6))
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

        # Save the figure
        plt.savefig(fig_name,dpi=300,bbox_inches='tight')

        if show_fig == False:
            plt.close(fig)
            plt.close(figure)
    
    # -------------------------------------------------------------------------

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
        # Figure name
        fig_name = filename + " Layer_thicknesses.png"

        # Initiate Figure
        fig2, ax2 = plt.subplots(figsize=(15, 11))
    
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

        # Control appearance
        ax2.invert_yaxis()
        ax2.set_aspect(0.2)
    
        # Label axes
        ax2.set_xlim([0.5,realization+1.5])
        ax2.set_ylabel('Depth')
        ax2.set_xlabel('Realization')
        fig2.suptitle('Randomized Layer Thicknesses After Merging')

        # Save the figure
        plt.savefig(fig_name,dpi=300,bbox_inches='tight')
        if show_fig == False:
            plt.close(fig2);
    
    # -------------------------------------------------------------------------
    


    ## Randomize tts

    # save inputs for correlation model in required format
    corr_model = [rho0, rho200, delta, d0, b];

    # randomize tts and return Vs
    Vs_all, tts_all, base_tts = tts_Rand_Vs(final_merged_depths, Depth, Vs, corr_model, sigmalntts, Vs_halfspace, delta_corr);


    # Extrapolate to a single depth
    Vs_all, tts_all, base_tts, Vs, Depth, final_merged_depths = extrapolate_plot(Vs_all, tts_all, base_tts, Vs, Depth, final_merged_depths, Nprofiles)

    # Calculate the standard deviation
    std_tts, std_Vs, depth_inter, median_tts, median_Vs = standard_deviation(Vs_all, tts_all, base_tts, Vs, Depth, final_merged_depths, Nprofiles)

    # Plot tts profile
    if fig_plot == True:
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
        ax4.set_title('Final Randomized tts Profiles')

        # Save the figure
        fig_name = filename + " Final_tts_profile.png"
        plt.savefig(fig_name,dpi=300,bbox_inches='tight')
        if show_fig == False:
            plt.close(fig4)
         
    
    # -------------------------------------------------------------------------
    # Plot final results
    #
    # -------------------------------------------------------------------------
        
    # Plot 2x2 figure
    if fig_plot == True:
        # Plotly subplots
        fig = make_subplots(rows=2, cols=2)

        # Plot Randomized Vs
        # Add scatter plot data to the first subplot
        fig.add_trace(go.Scatter(x=Vs_all[0], y=final_merged_depths[0], mode='lines', name='Randomized Vs',
                                 line=dict(color='gray', width=0.5), line_shape='vh',
                                 legendgroup="group1", hovertemplate='Randomized Vs'), row=1, col=1)
        for realization in range(Nprofiles):
            fig.add_trace(go.Scatter(x=Vs_all[realization], y=final_merged_depths[realization], mode='lines', 
                                     line=dict(color='gray', width=0.5), showlegend=False, line_shape='vh'), row=1, col=1)
            
        # Add base-case Vs to the subplot
        fig.add_trace(go.Scatter(x=Vs, y=Depth, mode='lines', name='Base-Case Vs', line_shape='vh', line=dict(color='black', width=1.2), 
                                 legendgroup="group1", hovertemplate='Base-Case Vs'), row=1, col=1)
        # Add median Vs to the subplot
        fig.add_trace(go.Scatter(x=median_Vs, y=depth_inter, mode='lines', name='Median', 
                                 line=dict(color='#90EE90', width=1.0, dash='dash'), 
                                 legendgroup="group1", hovertemplate='Median'), row=1, col=1)

        # Update axis properties
        fig.update_xaxes(title_text="Vs (m/s)", title_standoff=2, range=[0, None], row=1, col=1, side="top")
        fig.update_yaxes(title_text="Depth (m)", title_standoff=2, range=[Depth[-1], 0], row=1, col=1)

        # Plot std_Vs
        fig.add_trace(go.Scatter(x=std_Vs, y=depth_inter, mode='lines', name=r'$\sigma_{ln V_s}$'), row=1, col=2)

        # Update axis properties
        fig.update_xaxes(title_text=r'$\sigma_{ln V_s}$', title_standoff=2, range=[0, 0.5], row=1, col=2, side="top")
        fig.update_yaxes(title_text="Depth (m)", title_standoff=2, range=[Depth[-1], 0], row=1, col=2)

        
        # Plot Randomized tts
        # plot only 1 for legend
        fig.add_trace(go.Scatter(x=tts_all[0], y=final_merged_depths[0], mode='lines', line=dict(color='gray', width=0.5), 
                                 name='Randomized tts', legendgroup="group3", hovertemplate='Randomized tts'), row=2, col=1)
        for realization in range(Nprofiles):
            fig.add_trace(go.Scatter(x=tts_all[realization], y=final_merged_depths[realization], mode='lines',
                                     line=dict(color='gray', width=0.5), showlegend=False), row=2, col=1)
        
        # Add base-case tts to the subplot
        fig.add_trace(go.Scatter(x=base_tts, y=Depth, mode='lines', name='Base-Case tts', 
                                 line=dict(color='black', width=1.2), legendgroup="group3", hovertemplate='Base-Case tts'), row=2, col=1)

        # Add median tts to the subplot
        fig.add_trace(go.Scatter(x=median_tts, y=depth_inter, mode='lines', name='Median', 
                                 line=dict(color='#90EE90', width=1.0, dash='dash'), 
                                 legendgroup="group3", hovertemplate='Median tts'), row=2, col=1)
        
        # Update axis properties
        fig.update_xaxes(title_text="tts (s)", title_standoff=2, row=2, col=1, side="top", range=[0, None])
        fig.update_yaxes(title_text="Depth (m)", title_standoff=2, row=2, col=1, range=[Depth[-1], 0])

        # Plot std_tts
        fig.add_trace(go.Scatter(x=std_tts, y=depth_inter, mode='lines', name=r'$\sigma_{ln tts}$'), row=2, col=2)
        fig.add_vline(x=sigmalntts, line_color="red", row=2, col=2)
        fig.add_annotation(x=sigmalntts-0.007, y=Depth[-1]*0.95, text="Input: "+str(sigmalntts), 
                           showarrow=False, font=dict(color="red"), row=2, col=2)

        # Update axis properties
        fig.update_xaxes(title_text=r'$\sigma_{ln tts}$', title_standoff=2, row=2, col=2, range=[0, 0.1], side="top")
        fig.update_yaxes(title_text="Depth (m)", title_standoff=2, row=2, col=2, range=[Depth[-1], 0])

        # Update title and size
        fig.update_layout(
            title={
                'text': "Final Randomized Vs and tts Profiles",
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
        # Save the figure
        fig.write_html(filename + " Final_Vs_tts_profile.html")
        if show_fig == True:
            fig.show()
        

        
    # Save file of Vs
    if save_file == True:
        df1 = pd.DataFrame.from_dict(Vs_all, orient='index').transpose()
        df2 = pd.DataFrame.from_dict(final_merged_depths, orient='index').transpose()
        df = df1.join(df2,rsuffix=" Depth",lsuffix =" Vs")
        
        # sort columns
        idx = np.argsort([k[0:2] for k in df.columns])
        df = df.iloc[:,idx]
        df.to_csv("Randomized_Data.csv")
        

    return Vs_all, final_merged_depths, tts_all, base_tts, std_tts, std_Vs, depth_inter
