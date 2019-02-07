# -*- coding: utf-8 -*-
import os
import sys
import numpy as np
from struct import pack


# Import the pyArgus module
root_path = os.path.pardir#getcwd()
pyargus_path = os.path.join(os.path.join(root_path, "pyArgus"), "pyArgus")
sys.path.insert(0, pyargus_path)
import directionEstimation_v1p15 as de

####################################
#           PARAMETERS 
####################################

fname_template = "sim"
ch_no = 4
delays = [0, 0, 0, 0]
phase_shifts=[0, 0, 0,0]
blocks = 100
block_size = 1024*512


pn = 10**-3 # Noise power
fds= [] # File descriptors

# Antenna system parameters
M = 4  # Number of antenna elemenets 
UCA_radius = 0.5  # [wavelength]
ULA_spacing = 0.5 # [wavelength]
DOAs =  np.linspace(0,360, blocks)
antenna_array_type = "UCA"

if antenna_array_type == "UCA":
    x = UCA_radius * np.cos(2*np.pi/M * np.arange(M))
    y = UCA_radius * np.sin(-2*np.pi/M * np.arange(M))
    array_resp_vectors = de.gen_scanning_vectors(M, x, y, DOAs)
elif antenna_array_type == "ULA":    
    x = np.arange(M) * ULA_spacing
    y = np.zeros(M)
    array_resp_vectors = de.gen_scanning_vectors(M, x, y, DOAs)
    
else:
    print("[ ERROR ] Unidentified antenna array alignment")


####################################
#            Simulation
####################################

# Opening simulation files
for m in range(ch_no):
    fname=fname_template+str(m)+".iq"    
    fds.append( open(fname, 'w+b', buffering=0))
print("[ INFO ] All files opened")


signal = np.zeros((block_size), dtype=np.uint8)
raw_sig_nch = np.zeros((ch_no, block_size), dtype=np.uint8)

for b in range(blocks):
    print("[ INFO ] Writing block: %d"%b)
    raw_sig = np.random.normal(0,1,(block_size//2+max(delays)))+1j*np.random.normal(0,1,(block_size//2+max(delays)))
    raw_sig /= np.max(np.abs(raw_sig))
    raw_sig *= np.max(np.abs(raw_sig))*0.9         
    #raw_sig = np.exp(1j*2*np.pi*(100/(block_size//2+max(delays))) * np.arange((block_size//2+max(delays))))
    
    
    for m in range(ch_no):
        noise = np.random.normal(0,pn,(block_size//2+max(delays)))+1j*np.random.normal(0,pn,(block_size//2+max(delays)))
        # Use this to generate ULA simulation
        #raw_sig_m = raw_sig*np.exp(1j*2*np.pi*0.5*np.cos(np.deg2rad(0))*np.arange(4))[m]
        
        # Modifly the phase of received signal according to the realtive position of the element         
        raw_sig_m = raw_sig*array_resp_vectors[m,b]
        
        raw_sig_m += (1+1j)
        #raw_sig_m *= (255/2)
        raw_sig_m *= (255/2)
        raw_sig_nch[m,0::2] = raw_sig_m.real[delays[m]:delays[m]+block_size//2]
        raw_sig_nch[m,1::2] = raw_sig_m.imag[delays[m]:delays[m]+block_size//2]
      
        signal[0::2] = raw_sig_m.real[delays[m]:delays[m]+block_size//2]
        signal[1::2] = raw_sig_m.imag[delays[m]:delays[m]+block_size//2]      
        byte_array= pack('B'*block_size, *signal)         
        fds[m].write(byte_array)       
for f in fds:
    f.close()
print("[ DONE ] Al files are closed")
