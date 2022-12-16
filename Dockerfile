# -*- coding: utf-8 -*-
# @Author: Luis Condados
# @Date:   2022-02-07 20:39:25
# @Last Modified by:   Condados

# This is a Python 3 image that uses the nginx, gunicorn, fast api stack
# for serving inferences in a stable way.

# FROM tensorflow/tensorflow:2.10.0
FROM python:3.6.15-slim-buster

LABEL MAINTAINER Luis Condados condadoslgpc@gmail.com

ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update --fix-missing && apt-get install -y \
    # to avoid cv2 import error
    # ffmpeg libsm6 libxext6     \
    wget bzip2 ca-certificates \
    cmake build-essential      \
    pkg-config                 \
    python3-dev                \
    python3-pip                 \
    python3-setuptools          \
    python3-virtualenv          \
    nginx \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Here we get all python packages.
# There's substantial overlap between scipy and numpy that we eliminate by
# linking them together. Likewise, pip leaves the install caches populated which uses
# a significant amount of space. These optimizations save a fair amount of space in the
# image, which reduces start up time.

# Upgrade pip
RUN pip install --upgrade pip

# Install pip packages
RUN pip --no-cache-dir install  numpy\
                                idna\
                                gunicorn\
                                fastapi\
                                uvicorn[standard]\
                                "uvicorn[standard]" gunicorn\
                                transformers[sentencepiece] \
                                email-validator


# Set some environment variables. PYTHONUNBUFFERED keeps Python from buffering our standard
# output stream, which means that logs can be delivered to the user quickly. PYTHONDONTWRITEBYTECODE
# keeps Python from writing the .pyc files which are unnecessary in this case. We also update
# PATH so that the train and serve programs are found when the container is invoked.

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

# Set up the program in the image
COPY ./workspace /opt/program
WORKDIR /opt/program