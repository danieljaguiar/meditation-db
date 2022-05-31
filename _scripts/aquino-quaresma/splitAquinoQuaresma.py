from pymongo import MongoClient
from pathlib import Path
import requests
import re
import codecs
import json
import datetime
import os

initial_path = "./_scripts/aquino-quaresma/"

try:
    dir = initial_path + "output/"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
except OSError:
    pass

count_file = 17

with open(initial_path + "full - 012 - manulFixes.md", encoding="utf-8") as fullFile:
    lines = fullFile.readlines()

    for line in lines:
        if(line[0:1] == "#"):
            print(count_file + 1, "- new file ")
            count_file = count_file + 1
        else:
            with open(initial_path + "output/" + count_file.__str__() + ".md", "a", encoding="utf8") as newFile:
                newFile.write(line)
