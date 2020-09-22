#!/usr/bin/env python
# coding: utf-8

# ## Introducción
# 
# Sebastian Garcia 201630047
# 
# $ jupyter nbconvert --to script

# ### Ejercicio 2

# In[11]:


A = 5
B = 4
C = A + B
print(C)


# In[12]:


D = A ** 2
print(D)


# In[13]:


F = A / B # division
G = A // B # parte entera
H = A % B # modulo
print(F, G, H)


# In[14]:


mod = -5 % 4 
print(mod)


# ### Ejercicio 3

# In[17]:


hello = "Programación"
world = "Cientifica"
print(hello)
print(len(hello))


# In[18]:


hw = hello + ' ' + world
print(hw)


# In[27]:


s = "uniandes"

print(s.upper())
print(s.capitalize())

print(s.rjust(10))
print(s.center(14))
print(s.replace('n', 's'))

print(f'\n{s}')
print(r'Uni\nandes')
print('Uni\nandes')

print(3 * 'Uni' + 'andes')

print(s[3])
print(s[0:3])
print(s[4:])
print(s[1:-3])


# ### Ejercicio 4

# In[30]:


print("El número {}, es aproximadamente {}".format('PI', 3.1416))

print("El número {0}, es aproximadamente {1}".format('PI', 3.1416))

print("El número {num}, es aproximadamente {val}".format(num='PI', val=3.1416))

print("El número {0}, es aproximadamente {val}".format('PI', val=3.1416))


# ### Ejercicio 5

# In[32]:


print("Hay {:d} planetas en el sistema solar.".format(8))

print("{:.2f} (m/s2) es el valor de la aceleración gravitacional en la tierra.".format(9.80665))

print("bin: {0:b}, oct: {0:o}, hex: {0:X}".format(15))


# ### Ejercicio 6

# In[37]:


print("{:4}".format(18))

print("{:2d}".format(2290))

print("{:8.3f}".format(12.121212))

print("{:05d}".format(24))

print("{:08.3f}".format(12.231243))


# ### Ejercicio 7

# In[38]:


print("{:8.2f}".format(-8.349))
print("{:^8.2f}".format(-8.349))
print("{:<8.2f}".format(-8.349))
print("{:>8.2f}".format(-8.349))
print("{:=8.2f}".format(-8.349))


# In[40]:


print("{:10}".format("Uniandes"))
print("{:^10}".format("Uniandes"))
print("{:<10}".format("Uniandes"))
print("{:>10}".format("Uniandes"))
print("{:*^10}".format("Uniandes"))


# ### Ejercicio 8

# In[42]:


lista = ["Uniandes", 12, 3, 5, 8]

print(lista[0])
print(lista[-2])
print(lista[2:], '\n')

lista.append("Programacion")
print(lista)

del lista[3]
print(lista)

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letras)
letras[2:5] = ["C", "D", "E"]
print(letras)

letras[2:5] = []
print(letras)

new_lista = [lista, letras]
print(new_lista)


# ### Ejercicio 9

# In[43]:


vertebrados = {
    "Mamifero": ['vaca', 'perro', 'mono'],
    "Aves": ['aguila', 'colibri']
              }
vertebrados["Peces"] = ["yiburon", "salmon", "orca"]
print(vertebrados)

vertebrados.get("Aves")


# ### Ejercicio 10

# In[46]:


estudiante = {
    "nombre": "Sebastian",
    "apellido": "Garcia",
    "edad": 22,
    "carrera": "Ing Sistemas"
}

print("""
    {p[nombre]} {p[apellido]}, estudiante de {p[carrera]} tiene {p[edad]} años.
""".format(p=estudiante))

print("""
    {nombre} {apellido}, estudiante de {carrera} tiene {edad} años.
""".format(**estudiante))


# In[ ]:




