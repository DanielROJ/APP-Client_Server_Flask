#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:30:08 2019

@author: Daniel Rojas - danielroj

Script encargado de enviar un vector a un servidor utilizanodo el protocolo Http.
Asi mismo se encarga de imprimir la matriz transpuesta del vector enviado que recibe del servidor

"""

import requests as req
import json
import numpy as np

def  Go_Client():
    arr = np.array([],dtype=int); ## Se unicializa un vector vacio tipo Integer
    
    for i  in range(1,13): ## Se llena el vector con 12 pociciones
        arr = np.append(arr,i)
        pass
    string_arr = np.array2string(arr,separator=",") 
    js = json.dumps(string_arr) ##se convierte a json
    print("\n Se envia el siguiete Vector ")
    print(js + "\n")
    response = req.post("http://localhost:5000/index",json=js); ## Se envia la peticion Http al Servidor
    js_trans = response.json() ## Se recibe el Json respuesta del Servidor
    
    print("Se recibe del Servidor La siguiente Matriz")
    print(js_trans + "\n") ## Se imprime la Respuesta del servidor





Go_Client();


