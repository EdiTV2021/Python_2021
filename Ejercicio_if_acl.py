# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:38:53 2021

@author: Edison
"""

acl=int(input("Ingrese el valor de ACL: "))
if acl >=1 and acl<=99:
    print("La ACL es estandar")
elif acl >=100 and acl <=199:
    print("La ACL es extendida")
else: 
    print("el # ingresado no es de un ACL")
    