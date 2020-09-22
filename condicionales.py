#!/usr/bin/env python
# coding: utf-8

# Agosto 21, 2020 <br/>
# Sebastian Garcia 201630047
# 
# $ jupyter nbconvert --to script

# ### Condicionales

# In[1]:


if True:
    print(True)


# In[4]:


a, b, c, d = 2, 4, 3, 1
print(a > b)
print(c > d )
print(a < b and c > d and b > c)


# In[11]:


a = 5
b = 10

if b > a:
    print("b es mayor que a")

if b > a:
    print("{1} es mayor que {0}".format(a, b))
    


# In[13]:


_b = 5
if _b > 2:
    _b = _b ** 2
print(_b)


# In[14]:


a, b, c, d = 2, 4, 10, 1
if a > b or a < c and d < b:
    print("Entra al if")
    
print("End")


# In[17]:


anios = int(input("Edad?"))
if anios >= 18 and anios < 60:
    print("entra al bar")
elif (anios >= 60):
    print("No entra al bar")
else:
    print("no entra al bar, cedula?")


# In[20]:


if anios >= 18 and anios < 60 or anios > 90:
    print("entra")
else: 
    print("no entra")


# In[21]:


nota = float(input("nota?"))

if nota > 5.0:
    print("imposible!")
elif nota >= 4.5:
    print("exelente")
elif nota >= 3.0:
    print("buena")
else:
    print("perdió")


# ### Ejercicio 16

# In[24]:


cont = 0
while cont < 10:
    print(f'contador = {cont}')
    cont = cont + 1


# ### Ejercicio 17

# In[25]:


cont = 10
while cont > 0:
    print(f'contador = {cont}')
    cont = cont - 1


# In[26]:


numero = int(input("numero? "))
while numero < 0:
    print("numero negativo!")
    numero = int(input("numero? "))
    
print("numero positivo")


# In[ ]:




