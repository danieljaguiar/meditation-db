import sys
from pymongo import MongoClient
from pathlib import Path
import requests
import re
import codecs
import json
import datetime
import os
sys.path.append(os.path.abspath('./_scripts/main'))
import books

initial_path = "./_scripts/AlphonsusSundays/"


try:
    dir = initial_path + "output/"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
except OSError:
    pass


count_file = 0

with open(initial_path + "004 - Content.md", encoding="utf-8") as fullFile:
    lines = fullFile.readlines()

    for line in lines:
        if(line[0:2] == "# "):
            count_file = count_file + 1
        else:
            with open(initial_path + "output/" + count_file.__str__() + ".md", "a", encoding="utf8") as newFile:
                newFile.write(line)
