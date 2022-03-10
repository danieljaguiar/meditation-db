from pymongo import MongoClient
from pathlib import Path
import requests
import re
import codecs
import json
import datetime
import os

initial_path = "./_scripts/AquinasLent/"


try:
    dir = initial_path + 'outputlocal'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
except OSError:
    pass

count_file = 0

with open(initial_path + "AquinasLent-Full.md", encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        if(line[0:1] == "#"):
            print("new file", count_file)
            count_file = count_file + 1
        else:
            with open(initial_path + "outputlocal/AquinasLent-"+count_file.__str__()+".md", "a", encoding="utf8") as myfile:
                myfile.write(line)
