#!/usr/bin/env python
# coding: utf-8

# # Representación numerica
# Sebastian Garcia 201630047

# 156 => 10011100

# In[104]:


def decimalBinario(decimal): 
    if decimal > 1: 
        decimalBinario(decimal // 2) 
    print(decimal % 2, end = '') 
    
def binarioDecimal(binario): 
    decimal, i, n = 0, 0, 0
    while(binario != 0): 
        dec = binario % 10
        decimal = decimal + dec * pow(2, i) 
        binario = binario//10
        i += 1
    print(decimal) 


# In[105]:


# represnetacion Binaria y decimal

decimalBinario(15)
print()
decimalBinario(26)
print()
decimalBinario(127)
print()
decimalBinario(128)
print()
decimalBinario(511)
print()
decimalBinario(1024)
print()
print()
binarioDecimal(10011)
print()
binarioDecimal(111111)
print()
binarioDecimal(10010101)
print()
binarioDecimal(1110011)


# In[106]:


decimal = int('11111111', 2)
print(decimal)

binario = format(255 ,"b")
print(binario)


# represdentacion en 8 casillas: rango entre 0 y (2^8)-1

# In[4]:


print(format(15 ,"b"))


# In[5]:


print(format(26 ,"b"))


# In[6]:


print(format(1024 ,"b"))


# Para un sistema de N bits se pueden representar (2^N) elementos
# 
# ### Complementos
# 
# representación de nagativos
# 
# * Complemento a1 es invertir 1 <-> 0
# * Complemento a2 es sumarle 1 al LSB de a1
# 
# 4 => 100 => a1 => 011 => a2 => 100

# N bits generan 
# * (2^N) elementos; 
# * ((2^N)/2) - 1 elementos positivos; 
# * ((2^N)/2) negativos

# In[7]:


print(format(6 ,"b"))


# Con 8 bits se tienen 256 posibilidades, pero se logran 127 positivos y 128 negativos

# ### Complemento 2
# * Complemento (1) => flip 1 <=> 0
# * Complemento (2) => coger complemento (1) y de derecha a izquierda, ir cambiando 1's por 0's hasta encontrar el primer 0. Cambiar ese cero por un 1 y terminar.

# Complemento (2) de **1100** => 0011 => **0100**

# In[138]:


def complemento_dos(binario, bits):
    if (binario & (1 << (bits - 1))) != 0: 
        binario = binario - (1 << bits)        
    return binario                         


def complemento_dos_decimal(n, N):
    print('Decimal:', n)
    print('Binario:', format(abs(n), "b"))

    complemento = format(abs(n) ^(1 << N) - 1 , "b")
    for i in range(N):
        if len(complemento) < N:
            complemento = "0" + complemento
    print('a1:',complemento)

    compl_dos = [x for x in complemento]
    for i in range(N-1, 0, -1):
        if complemento[i] == "1":
            compl_dos[i] = "0"
        else: 
            compl_dos[i] = "1"
            break

    print("a2: ", end="")
    for x in compl_dos:
        print(x, end="")
    print()
    print()
   
# n = -116 # numero decimal
N = 8 # bits
numeros = [-116, 127, 134, -128]

for x in numeros:
    complemento_dos_decimal(x, N)


# In[ ]:




