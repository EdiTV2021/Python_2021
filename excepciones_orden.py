# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 19:03:58 2021

@author: Edison
"""

#excepciones
try:
    y=1/0
except ArithmeticError:
    print("Error aritmético")
    
except ZeroDivisionError:
    print("No puedes dividir para cero")
    