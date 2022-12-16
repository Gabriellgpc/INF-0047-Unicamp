#!/bin/bash
#
# @Author: Condados
# @Date:   2022-12-16 16:27:09
# @Last Modified by:   Condados
# @Last Modified time: 2022-12-16 16:27:44

docker build . -t t5-translation-fastapi:latest

docker run -it --rm --p 8000:8000 t5-translation-fastapi:latest serve