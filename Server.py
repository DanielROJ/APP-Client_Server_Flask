#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:22:04 2019

@author: droro
"""

from flask import Flask

from flask import request as req

import json



app = Flask(__name__);


@app.route("/index",methods=['GET', 'POST'])

def index():
    js = req.json;
    
    arr = json.loads(js);
    arr = arr.split()
    print(arr)
    
    
    return "ok"
    


app.run(port=5000)

