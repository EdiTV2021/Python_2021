# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:23:36 2021

@author: Edison
"""

def saludos(lista):
    for puntero in lista:
        print("Hola", puntero)
    print(" ")
    
saludos(["Juan"])
saludos(["Juan", "Ana"])
saludos(["Juan", "Ana","Dillan"])