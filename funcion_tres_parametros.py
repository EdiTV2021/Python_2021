# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:24:27 2021

@author: Edison
"""

def direccion(provincia,ciudad,barrio):
    print("Su dirección es: ")
    print("Su provincia es: ", provincia)
    print("La ciudad de domicilio es:", ciudad)
    print("La dirección de referencia es: ", barrio)
    

pr=input("Ingrese la provincia: ")
br=input("Ingrese el barrio: ")
ci=input("ingrese la ciudad:")

direccion(pr,ci,br)
direccion(provincia=pr,ciudad=ci,barrio=br)
direccion(provincia=pr,barrio=br,ciudad=ci)