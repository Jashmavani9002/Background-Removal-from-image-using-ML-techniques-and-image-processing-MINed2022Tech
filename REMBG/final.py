# Importing modules
import time
import os,sys
from os import listdir
import subprocess

# starting a timer
start = time.perf_counter()

# Data folder path
# It can be Absolute or relative
try :
    base = sys.argv[1]
except :
    print("Provide path to folder -----  python final.py 'path/to/folder' ")

# collecting all folders from Given Path
temp = [f"{base}/{f}" for f in listdir(base)]
all_folder = [f"{base}/{f}" for f in listdir(base) if "output" not in f]


# Processing for all folder one by one
for one_folder in all_folder :
    of_time = time.perf_counter()
    outputpath = one_folder + "_output"
    if  outputpath in temp :
        continue
    else :
        os.makedirs(outputpath)

    # rembg p Shape_1d_256i/SEM Shape_1d_256i/SEM_output
    subprocess.run(["rembg","p",one_folder,outputpath],stderr=sys.stderr, stdout=sys.stdout) 
    print(f"Time for {one_folder} to be processed is {time.perf_counter()-of_time}")
    

#  Printing total time for the process
print(time.perf_counter()-start)