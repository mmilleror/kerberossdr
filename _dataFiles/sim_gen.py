# -*- coding: utf-8 -*-
import numpy as np
from struct import pack
import matplotlib.pyplot as plt

fname_template = "sim"
ch_no = 4
delays = [0, 10, 20, 30]
phase_shifts=[0, 45, 0,0]
blocks = 100
block_size = 1024*512

fds= [] # File descriptors
for m in range(ch_no):
    fname=fname_template+str(m)+".iq"    
    fds.append( open(fname, 'w+b', buffering=0))
print("All files opened")
signal = np.zeros((block_size), dtype=np.uint8)
raw_sig_nch = np.zeros((ch_no, block_size), dtype=np.uint8)
for b in range(blocks):
    print("Writing block: %d"%b)
    raw_sig = np.random.normal(0,1,(block_size//2+max(delays)))+1j*np.random.normal(0,1,(block_size//2+max(delays)))
    #raw_sig = np.exp(1j*2*np.pi*(100/(block_size//2+max(delays))) * np.arange((block_size//2+max(delays))))
    
    for m in range(ch_no):        
        raw_sig_m = raw_sig*np.exp(1j*np.deg2rad(phase_shifts[m]))        
        raw_sig_m += (1+1j)
        raw_sig_m *= (255/2)
        raw_sig_nch[m,0::2] = raw_sig_m.real[delays[m]:delays[m]+block_size//2]
        raw_sig_nch[m,1::2] = raw_sig_m.imag[delays[m]:delays[m]+block_size//2]
        
        
        signal[0::2] = raw_sig_m.real[delays[m]:delays[m]+block_size//2]
        signal[1::2] = raw_sig_m.imag[delays[m]:delays[m]+block_size//2]      
        byte_array= pack('B'*block_size, *signal)         
        fds[m].write(byte_array)       
for f in fds:
    f.close()
print("Al files are closed")
"""
iq_samples = np.zeros((ch_no, block_size//2), dtype=complex)
for m in range(ch_no):   
    real = raw_sig_nch[m, 0 ::2]
    imag = raw_sig_nch[m, 1::2]
    iq_samples[m,:].real, iq_samples[m,:].imag = real, imag
    iq_samples /= (255 / 2)
    iq_samples -= (1 + 1j)

pw=2**15
offset = 50000
delay = 0
phasors = (iq_samples[0, offset: pw+offset] * iq_samples[1, offset+delay: pw+offset+delay].conj())
phasors /= np.abs(phasors)
#K = 1000
#plt.scatter(phasors.real, phasors.imag)
xw = np.abs(np.fft.fft(iq_samples[1,:]))
#plt.plot(iq_samples[3,:].imag)
plt.plot(xw)
"""
