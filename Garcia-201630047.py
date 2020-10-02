#!/usr/bin/env python
# coding: utf-8

# # Parcial 2
# 201630047

# ### Punto 1

# In[23]:


##
import struct
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np

print("--")
#se encuentra una serie de datos de números enteros con signo, cada uno almacenado en 16 bits
#promedio : 32.3238636
file_name = "DataFileImpar.bin"
with open(file_name, 'rb') as f:
    x = f.read()
    valores = np.double(struct.unpack("h"*int(len(x)/2), x)) # size double => 8B
    print("Promedio esperado: ", f'{np.mean(valores):0.7f}' == '32.3238636', f'{np.mean(valores):0.7f}' )
    print("Size: ", len(valores))
    print("Min: ", np.min(valores))
    print("Max: ", np.max(valores))
    print("Multiples de 7: ", len([ x for x in valores if x % 7 == 0 ]))
    print("Valores entre -3 y 16: ", len([ x for x in valores if x >= -3 and x <= 16 ]))
    print("Media de Valores entre -3 y 16: ", np.mean([ x for x in valores if x >= -3 and x <= 16 ]))


# In[24]:


2400 / 2


# In[25]:


2400 / 8


# In[26]:


2400 / 4


# ### Punto 6

# In[36]:



def punto(N, x=0.34):
    # condicion de parada
    if N < 0: return 0
    arriba = ((3 + ((2 * x)/(N + 1)) ) + (x ** ((5 * N) + 1)))
    abajo = (N + 2)
    return ( arriba / abajo ) + punto(N=N-1)

for n in [0, 5, 16, 55, 103, 156]:
    val = punto(N=n)
    print(f'N: {n} ==> {val:0.4f}')


# In[38]:


import math
print(math.log2(25.567))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




