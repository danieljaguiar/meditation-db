from pymongo import MongoClient
from pathlib import Path
import requests
import re
import codecs
import json
import datetime
import os

try:
    dir = './AquinasLent'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
except OSError:
    pass

count_file = 0

with open("./_scripts/AquinasLent/full3.md", encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        if(line[0:1] == "#"):
            print("new file", count_file)
            count_file = count_file + 1
        else:
            with open("./_scripts/AquinasLent/output/"+count_file.__str__()+".md", "a", encoding="utf8") as myfile:
                myfile.write(line)
