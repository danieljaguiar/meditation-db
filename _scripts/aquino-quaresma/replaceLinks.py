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

initial_path = "./_scripts/aquino-quaresma/"

regexp = re.compile(
    r'\((([1-4]{1,2}\s)?[^\s\[]*)\s([0-9]{1,3}),\s?([^\)]*)\)', re.MULTILINE)

count_file = 0

with open(initial_path + "full - 010 - manual review.md", encoding="utf-8") as fullFile:
    lines = fullFile.readlines()

    with open(initial_path + "/full - 011 - fixedLinks.md", "a", encoding="utf8") as newFile:
        for line in lines:
            res = regexp.search(line)
            while res:
                res = regexp.search(line)
                book = res.group(1)
                chapter = res.group(3)
                verse = res.group(4)

                # if check_int(chapter):
                #     newInt = int(chapter)
                # else:
                #     try:
                #         newInt = roman.fromRoman(chapter.upper())
                #     except:
                #         print("no roman", res.group(0), line)

                if book not in books.conv:
                    print(res.group(1))
                    line = line.replace(res.group(0), "(BROKEN)")
                else:
                    line = line.replace(res.group(0), "([" + books.conv[book] + ". " + chapter + ", " + verse.strip() + "](https://vulgata.online/bible/" +
                                        books.conv[book] + "." + chapter + "?ed=MS&vfn=MS." + books.conv[book] + "." + chapter + "." + verse.strip() + ":vs))")

                res = regexp.search(line)

            newFile.write(line)
