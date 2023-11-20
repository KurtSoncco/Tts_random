# Travel time randomization to account Spatial Variability in 1D Ground Response Analysis

Based on Prof. Mohamad Hallal et al. [[1]](#1) paper, the following uses the Travel Time Randomization method to create N profiles for Spatial Variability analysis.

<p align="center">
<img src="Code\4x4.png" alt="Ouput" width="450"/>
</p>

## Input 
The folllowing code requires a csv file with the data of Vs and Depth of each layer. (Currently, the code is using S.I. units).

* CSV file with Depth and Vs values (in S.I. Units)

## Output
The code is currently exporting a CSV file with the randomized number of profiles and an output for the selected 1D GRA analysis software used. 

## References
<a id="1">[1]</a> 
Mohamad M. Hallal, Brady R. Cox, Sebastiano Foti, Adrian Rodriguez-Marek, Ellen M. Rathje,
Improved implementation of travel time randomization for incorporating Vs uncertainty in seismic ground response,
Soil Dynamics and Earthquake Engineering,
Volume 157,
2022,
107277,
ISSN 0267-7261,
https://doi.org/10.1016/j.soildyn.2022.107277.
(https://www.sciencedirect.com/science/article/pii/S0267726122001269)
