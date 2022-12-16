# -*- coding: utf-8 -*-
# @Author: Luis Condados
# @Date:   2022-02-07 20:38:20
# @Last Modified by:   Condados
# @Last Modified time: 2022-12-16 15:59:04
# Contact: condadoslgpc@gmail.com

from fastapi import FastAPI
from source.base_classes import *

title='T5 Machine Translation'
description='''

'''
version='v1.0'
# contact = {'name': 'Luis Condados', 'email': 'condadoslgpc@gmail.com'}
# license_info= {'name': 'All Rights Reserved'}
# The fastapi app for serving predictions
app = FastAPI(title=title,
              description=description,
              version=version,
              debug=True,
              )

@app.get("/ping", tags=['Health Check'])
def ping():
    """
        # Determine if the container is working and healthy.
        We declare it healthy if we can load all models successfully.
    """
    # You can insert a health check here
    return 200

@app.post("/predict/", tags=['Model'])
def invocation(request: RequestTemplate):

    sentence = request.sentence
    # model inference ...
    response = {'translation':sentence}
    return response