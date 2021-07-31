# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 20:23:41 2021

@author: Edison
"""

listar=[]
listas=[]
lista=["R1","R2","R3","R4"
       ,"S1", "S2"]
for item in lista:
    if "S" in item:
        #Para llenar los valores de una lista
        listas.append(item)
print("Lista de datos de S")
print(listas)
for item in lista:
    if "R" in item:
        #Para llenar los valores de una lista
        listar.append(item)
print("Lista de datos de R")
print(listar)
        