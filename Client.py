#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:30:08 2019

@author: Daniel Rojas 

Script encargado de enviar un vector a un servidor utilizanodo el protocolo Http

"""

import requests as req
import json
import numpy as np

def  Go_Client():
    arr = np.array([],dtype=int);
    
    for i  in range(1,13):
        arr = np.append(arr,i)
        pass
    string_arr = np.array2string(arr,separator=",")
    js = json.dumps(string_arr)

    response = req.post("http://localhost:5000/index",json=js);
    print(response.status_code)





Go_Client();


