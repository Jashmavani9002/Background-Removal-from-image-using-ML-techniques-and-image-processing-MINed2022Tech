# BG Removel Using REMBG library

<hr>

rembg python module is used for bg remove for image. It uses U<sup>2</sup>Net which is silent object detection ML technique which is already developed. 

> # requirnments

- python version = >=3.8
- rembg 

> # How to  run

- Install python 3.8 or 3.9

```bash 
$sudo apt install python3.8
```

- Install Pip for installing modules

```bash 
$sudo apt install python3-pip
```

- Create vitual environment and activate it (Activation Method Depends on OS)

```bash 
$pip install virtualenv
$virtualenv venv
$source venv/bin/activate
```

- Insatll all requriments

```bash 
$pip install -r requirements.txt
```

- Run file with command line argument of path to data folder

```bash 
$python final.py 'path/to/folder'
```

## Current image processing speed is 1.5 sec/image

## Speed Increasing Techniques
### - Using GPU
    - Library provides GPU support

```bash 
$pip install rembg[gpu]
```
### - Using Threadpool
    - Applying Threadpool executor using more workers parallely
    - It depends on CPU performance