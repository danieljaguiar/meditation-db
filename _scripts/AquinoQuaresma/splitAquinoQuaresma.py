from pymongo import MongoClient
from pathlib import Path
import requests
import re
import codecs
import json
import datetime
import os

initial_path = "./_scripts/AquinoQuaresma/"


try:
    dir = './AquinoQuaresma'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
except OSError:
    pass

count_file = 0

with open(initial_path + "full.md", encoding="utf-8") as fullFile:
    lines = fullFile.readlines()

    with open(initial_path + "slugList.txt", encoding="utf-8") as fileNames:
        fileNamesLines = fileNames.readlines()

        for line in lines:
            if(line[0:1] == "#"):
                count_file = count_file + 1
                print(count_file, "- new file - ",
                      fileNamesLines[count_file].strip())
            else:
                with open("./AquinoQuaresma/"+count_file.__str__()+".md", "a", encoding="utf8") as newFile:
                    newFile.write(line)
