# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 20:36:52 2021

@author: Edison
"""

def l100kmtompg(litros):
    millas= 100000/1609.344
    galones= litros/3.785411784
    return millas/galones

def mpgtol100km(millas):
    metros=millas*1609.344/100000
    litros= 3.785411784
    return litros/metros

#resultados
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
    