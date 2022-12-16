#!/bin/bash
#
# @Author: Condados
# @Date:   2022-12-16 16:27:09
# @Last Modified by:   Condados
# @Last Modified time: 2022-12-16 16:27:44

docker build . -t t5-translation-fastapi:latest

docker run -it --rm --p 8000:8000 t5-translation-fastapi:latest serve

# gunicorn --timeout 300 -k sync -b unix:/tmp/gunicorn.sock -w 2 wsgi:app --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# 'gunicorn',
#                                  '--timeout', str(model_server_timeout),
#                                  '-k', 'sync',
#                                  '-b', 'unix:/tmp/gunicorn.sock',
#                                  '-w', str(model_server_workers),
#                                  'wsgi:app',
#                                  '--worker-class','uvicorn.workers.UvicornWorker',
#                                  '--bind', '0.0.0.0:8000'