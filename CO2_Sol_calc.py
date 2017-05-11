#---------------------------------------------------------------------------
# 4/16/17
# Author: Jacob Zahn
# Calculating CO2 and Solar Forcings over Earth's History
#---------------------------------------------------------------------------

# Those Sweet Imports
#---------------------------------------------------------------------------
import numpy as np
import CO2_Sol_globals as gl
import model as md


# Calculating Forcings
#---------------------------------------------------------------------------
class CO2_fab_Forcing(object):

    def __init__(self,C0,C_fab):
        self.aa = np.log(gl.C0**-1*gl.C_fab)          # First term in CO2 Forcing
        self.bb = (np.log(gl.C0**-1*gl.C_fab))**2     # Second Term in CO2 Forcing
        self.dFCO2 = 5.32*self.aa+0.39*self.bb        # CO2 Forcing [W/m2]


class CO2_mea_Forcing(object):

    def __init__(self,C0,C_mea):
        self.aa = np.log(gl.C0**-1*gl.C_mea)          # First term in CO2 Forcing
        self.bb = (np.log(gl.C0**-1*gl.C_mea))**2     # Second Term in CO2 Forcing
        self.dFCO2 = 5.32*self.aa+0.39*self.bb        # CO2 Forcing [W/m2]

    
class Solar_Forcing(object):

    def __init__(self,Fst,Fs,A):
        self.dFSol = ((gl.Fst-gl.Fs)*(1-gl.A))/4      # Solar Forcing [W/m2]
        self.dFSol_lat = ((gl.Fst_lat-gl.Fs_lat)*(1-gl.A))/4      # Solar Forcing [W/m2]

        
for ii in range(len(gl.C_fab)):                       # Creating Forcing Arrays
    gl.dFCO2_fab[ii] = CO2_fab_Forcing(gl.C0,gl.C_fab).dFCO2[ii]
    gl.dFCO2_mea[ii] = CO2_mea_Forcing(gl.C0,gl.C_mea).dFCO2[ii]
    gl.dFSol[ii] = Solar_Forcing(gl.Fst,gl.Fs,gl.A).dFSol[ii]
    gl.dF_fab[ii] = gl.dFCO2_fab[ii]+gl.dFSol[ii]
    gl.dF_mea[ii] = gl.dFCO2_mea[ii]+gl.dFSol[ii]
    
for ii in range(len(md.lat)):
    gl.dFSol_lat[ii] = Solar_Forcing(gl.Fst_lat,gl.Fs_lat,gl.A).dFSol_lat[ii]
    gl.dFCO2_mea_single[ii] = gl.dFCO2_mea[-1]