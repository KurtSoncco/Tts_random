# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 16:23:28 2023

@author: kurt-
"""

import pandas as pd
from Code import Travel_time
from deepsoil import deepsoil_input
from strata_output import strataPy_output

## Load Input Vs Profile
# The Vs profile can be loaded in different ways. You can read from a .txt
# file, or any other format. You will just have to add the code to read the
# Vs profile. For this example, we are loading a Vs profile saved as a .mat
# file. Regardless of the format, you need 2 vectors 'Vs' and 'Depth'. Ig
# the variables are named in any different way (including capitalization),
# parts of the code will need to be edited.
# Both Vs and Depth are 1D arrays/vectors. Depth starts at ground surface
# (0 is the first value) and ends at the halfspace depth. The different
# values in between are depths to different layer interfaces. 
# Vs follows the same format as Depth, with first value being shear wave
# velocity of first layer, etc..., and last value being the Vs of the
# halfspace/bedrock.
mat = pd.read_csv("Code\Example_Profile.csv",header=None, names=['Depth','Vs'])
Depth = mat['Depth'].values.reshape(-1)
Vs = mat['Vs'].values.reshape(-1)

## Run Travel_time function
Vs_all, depth_all, tts_all, base_tts, _, _, _ = Travel_time(Vs, Depth, show_fig=True)
#deepsoil_input(Vs_all,depth_all)
#strataPy_output(Vs_all,depth_all)








