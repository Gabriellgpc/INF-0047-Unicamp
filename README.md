# Serving the BERT model with Fast API

Classifier model BERT based.

# Requirements

You'll have to install docker and docker-compose to run this project more smoothly.
Official instructions here:
- [Docker install](https://docs.docker.com/engine/install/)
- [Docker-compose install](https://docs.docker.com/compose/install/)

# How to run
You have to put your trained model whithin `workspace/assets/saved_model` and your **preprocessor** in `workspace/assets/saved_preprocessor`.
After that just launch the docker-compose:

```
$ docker-compose up --build
```

After the docker building a server containning the fastapi will be avaible. You'll see the documentation at [http://localhost:8000/docs](http://localhost:8000/docs)

# Struct of this project

```
bert-model-with-fast-api
├── docker-compose.yml
├── Dockerfile
├── notebooks 
│   └── inference.ipynb # example of how do the requests
├── README.md
├── requirements.txt
└── workspace
    ├── assets
    │   ├── README.md
    │   ├── saved_model
    │   │   ├── assets
    │   │   │   └── vocab.txt
    │   │   ├── keras_metadata.pb
    │   │   ├── saved_model.pb
    │   │   └── variables
    │   │       ├── variables.data-00000-of-00001
    │   │       └── variables.index
    │   └── saved_preprocessor
    │       ├── assets
    │       │   └── vocab.txt
    │       ├── keras_metadata.pb
    │       ├── saved_model.pb
    │       └── variables
    │           ├── variables.data-00000-of-00001
    │           └── variables.index
    ├── nginx.conf      #Configuration file of the nginx server manager 
    ├── predictor.py    #FastAPI functionalities
    ├── serve           #To launch the server
    ├── source          #Folder with the classes definitions ans auxiliary functions
    │   ├── base_classes.py 
    │   ├── __init__.py
    │   └── model.py
    ├── utils
    │   ├── __init__.py
    │   └── set_gpu.py
    └── wsgi.py      #That's just a wrapp program
```

How to enable the GPU use:

Useful tutorials: 
- 

- If you do not have the driver of  the GPU installed. Try to use `$nvidia-smi`, if works you already have the driver installed, if not ([a good tutorial](https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-20-04-focal-fossa-linux)):
    `sudo ubuntu-drivers autoinstall`

- Follow this instruction to install the cuda toolkit: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker
