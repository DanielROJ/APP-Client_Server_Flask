#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:22:04 2019

@author: Daniel Rojas - danielroj

Script encargado de funcionar como servidor utlizando el protocolo http,
Asi mismo, se encarga de recibir un JSON con un vector y convertirlo en una matriz transpuesta y enviarselo al cliente de origen de nuevo

"""

## Se importan las librerias necesarias
from flask import Flask

from flask import request as req

import json

import numpy as np

##Se inicializa el Servidor
app = Flask(__name__);


##Se establece la ruta para atender la peticion y el tipo de metodo Http
@app.route("/index",methods=['GET', 'POST'])

def index():
    js = req.json;    ##Recibe el json de un cliente
    arr = json.loads(js); ## Convierte el json a String
    
    list_l = str(arr).replace("[","").replace("]","").replace(" ","").split(",") ##Elimina Simbolos innecesarios
    
    numL= np.array([]);
    for i in list_l:  ## Convierte cada simobolo a tipo Integer
        numL=np.append(numL,int(str(i).replace(" ","")));
        pass
    
    ## Se Define Tamanio de la Matriz Trnaspuesta
    num_column=4; 
    num_row=3;
    a=0;
    b= num_column;
    matriz = [];  
    for i in range(1,num_row +1): ##Se llena la Matriz segun los limites establecidos
            auxL = np.array(numL[a:b]);
            a+=4;
            b+=4;
            
            matriz.append(auxL) ##Anida cada fila
            pass
    matriz = np.array(matriz) 
    trans = matriz.transpose() ## Saca la transpuesta de la Matriz Creada
    str_trans = np.array_str(trans) ## Se convierte a String
    js_trans = json.dumps(str_trans) 
    print(js_trans) 
        
    
    
    return  js_trans ## Se convierte y se retorna un JSON
    


app.run(port=5000)

