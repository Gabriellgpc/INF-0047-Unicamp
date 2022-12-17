# -*- coding: utf-8 -*-
# @Author: Luis Condados
# @Date:   2022-02-07 20:38:20
# @Last Modified by:   Condados
# @Last Modified time: 2022-12-16 15:59:04
# Contact: condadoslgpc@gmail.com

from transformers import pipeline
from fastapi import FastAPI
from source.base_classes import *

title='T5 Machine Translation - Machine 1'
description='''
Rest API service for English to Germany translation.
'''
version='v1.0'
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
    # model inference
    translator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
    outputs = translator(sentence, clean_up_tokenization_spaces=True)
    response = {'translation':outputs[0]['translation_text']}
    return response