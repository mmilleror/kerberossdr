# -*- coding: utf-8 -*-



import time
import numpy as np
fd = open("/ram/DOA_value.html","w")
for i in range(360):
    DOA = int(i+np.random.normal(0,3))
    DOA_str = str(DOA)         
    DOA_str += ' ' * (4-len(DOA_str))
    html_str = "<DOA>"+DOA_str+"</DOA>"
    fd.seek(0)    
    fd.write(html_str)
    print(html_str)
    time.sleep(0.2)
fd.close()
