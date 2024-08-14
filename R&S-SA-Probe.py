import pyvisa
import numpy as np
import matplotlib.pyplot as plt

# This script communicates with a Spectrum Analyzer 
# that utilizes SCPI commands 
# The method of connection is with a GPIB bus
# Author: Johann Lee    Version ----
# Date: ----

# Required Drivers:
# NI 488.2 (Assuming NI GPIB to USB)

# Input Variables
filePathDatWrite = 'INSERT PATH LOCATION'
filePathMatWrite = filePathDatWrite
fileNamesWrite = 'FILE NAME'
fileExtensionWrite = '.dat'

options = {
    "write_data": True, # Write output into .dat files
    "plot_color": "Manual",
}

# initialize GPIB communications
rm = pyvisa.ResourceManager()
instrument = rm.open_resource('GPIB0::16::INSTR') # Port at which computer will communicate with machine
instrument.timeout = 10000 # Buffer time to allow machine to output data (milliseconds)  
print('Instrument Connection Success\nTesting Feedback') 

# clear past data and clarify machine ID
instrument.clear()
instrument.query('*IDN?') # Asks machine for ID and model

#####

# ONCE SUCCESSFULL CONNECTION
# SCRIPT FOR MEASUREMENT GOES HERE 

#####