# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 18:53:46 2021

@author: Edison
"""

#excepciones
try:
    x=int(input("Ingrese un numero: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir para cero")
except ValueError:
    print("No ingresaste un valor entero")
except: 
    #ayuda a controlar varias excepciones
    #ejm Ctrl + C
    print("Oh dear, algo fue mal...")
print("Fin")