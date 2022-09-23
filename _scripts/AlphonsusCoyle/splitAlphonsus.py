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
from pathlib import Path
import shutil


initial_path = "./_scripts/AlphonsusCoyle/"

try:
    shutil.rmtree(initial_path + "output/")
except OSError:
    pass


Path(initial_path + "output/").mkdir(parents=True, exist_ok=True)
Path(initial_path + "output/alphonsus-morning").mkdir(parents=True, exist_ok=True)
Path(initial_path + "output/alphonsus-evening").mkdir(parents=True, exist_ok=True)
Path(initial_path + "output/alphonsus-spiritual").mkdir(parents=True, exist_ok=True)

mm = 10000
ev = 20000
sr = 30000


with open(initial_path + "test.csv", "a", encoding="utf8") as finalJSON:
    with open(initial_path + "007 - Manual Corrections/all.md", encoding="UTF-8") as fullFile:
        lines = fullFile.readlines()

        overline = ""

        for line in lines:
            lineStripped = line.strip()
            # print(line[0:5] + "xxxxx")

            if(lineStripped[0:2] == "# "):
                overline = lineStripped[2:]
                continue

            if(lineStripped[0:3] == "## "):
                # this should generate a new file handle
                headInfo = lineStripped[3:]
                headParts = headInfo.split(" -- ")
                fileName = ""
                if(headParts[0] == "Morning Meditation"):
                    mm = mm + 1
                    fileName = "alphonsus-morning/" + mm.__str__()
                if(headParts[0] == "Evening Meditation"):
                    ev = ev + 1
                    fileName = "alphonsus-evening/" + ev.__str__()
                if(headParts[0] == "Spiritual Reading"):
                    sr = sr + 1
                    fileName = "alphonsus-spiritual/" + sr.__str__()

                file = open(initial_path + "output/" +
                            fileName + ".md", "a", encoding="utf8")

                finalJSON.write(fileName + "$" + overline + "$" +
                                headParts[0] + "$" + headParts[1] + '\n')

                continue

            if("file" in locals()):
                file.write(lineStripped + '\n')

        # else:
        #     # res = regexp.search(line)
        #     # while res:
        #     #     res = regexp.search(line)
        #     #     book = res.group(1)
        #     #     chapter = res.group(3)
        #     #     verse = res.group(4)

        #     #     # if check_int(chapter):
        #     #     #     newInt = int(chapter)
        #     #     # else:
        #     #     #     try:
        #     #     #         newInt = roman.fromRoman(chapter.upper())
        #     #     #     except:
        #     #     #         print("no roman", res.group(0), line)

        #     #     if book not in books.conv:
        #     #         print(res.group(1))
        #     #         line = line.replace(res.group(0), "(BROKEN)")
        #     #     else:
        #     #         line = line.replace(res.group(0), "([" + books.conv[book] + ". " + chapter + ", " + verse.strip() + "](https://vulgata.online/bible/" +
        #     #                             books.conv[book] + "." + chapter + "?ed=MS&vfn=MS." + books.conv[book] + "." + chapter + "." + verse.strip() + ":vs))")

        #     #     res = regexp.search(line)

        #     with open(initial_path + "output/" + count_file.__str__() + ".md", "a", encoding="utf8") as newFile:
        #         newFile.write(line)
