#---------------------------------------------------------------------------
# 4/18/17
# Author: Jacob Zahn
# Global Variables for CO2 & Solar Forcing Model
#---------------------------------------------------------------------------

# Those Sweet Imports
#---------------------------------------------------------------------------
import numpy as np
import pandas as pd
import model as md
import os

# Loading CO2 Data
#---------------------------------------------------------------------------
sheet_title = 'LOESS Fit'
fn = os.path.join(os.path.dirname(__file__), 'ncomms14845-s3-2.xlsx')
data = pd.read_excel(fn, sheetname = sheet_title, header = 2)
data.columns = ['Age [Ma]','Atmospheric CO2 [ppm]','LW95','LW68','UP68','UP95']


# Defining Constants & Variables
#---------------------------------------------------------------------------
Fs = 1368                              # Present-day Total Solar Irradiance [W/m2]
Fs_lat = md.S_final[:,-1]
A = 0.3                                # Average Albedo of Earth
t0 = 4570                              # Age of the Earth [Myrs]
t_intermediate = data['Age [Ma]']      # Time Array (size = 838)

# Loop to convert t values from "My before present" to My since Earth Formation"
#---------------------------------------------------------------------------
t = np.zeros(len(t_intermediate))
for ii in range(len(t_intermediate)):
    t[ii] = 4700 - t_intermediate[ii]
#---------------------------------------------------------------------------
    
C0 = 278                                         # Pre-Industrial CO2 [ppm]
C_fab = np.arange(400,2000,1.9094)               # Fabricated CO2 data (size = 838)
C_mea = data['Atmospheric CO2 [ppm]']            # Real CO2 data (size = 838)
dFCO2_fab = np.zeros(len(t))                     # Initializing CO2 forcing Array
dFCO2_mea = np.zeros(len(t))                     # Initializing CO2 forcing Array
dFCO2_mea_single = np.zeros(len(md.lat))         # Initializing CO2 forcing Array
dFSol = np.zeros(len(t))                         # Initializing Solar forcing Array
dFSol_lat = np.zeros(len(md.lat))
dF_fab = np.zeros(len(t))                        # Initializing Combined forcing Array
dF_mea = np.zeros(len(t))                        # Initializing Combined forcing Array
Fst = Fs/(1+(0.4*(1-t0**-1*t)))                  # TSI over last 400 [W/m2]
Fst_lat = Fs_lat/(1+(0.4*(1-t0**-1*t[-1])))                  # TSI over last 400 [W/m2]