import roman
from pymongo import MongoClient
from pathlib import Path
import requests
import re
import codecs
import json
import datetime
import os
import sys
sys.path.append(os.path.abspath('./_scripts/main'))
# don't
import books


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


regexp = re.compile(
    r'\[\[([^\s|^\.]*)[\s|\.|,]*([^\,|^\s|^\.]*)[\,|\s|\.]([^\]]*)\]\]', re.MULTILINE)

count = 0

with open("./_scripts/AquinasLent/full2.md", encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        res = regexp.search(line)

        while res:
            book = res.group(1)
            chapter = res.group(2)
            verse = res.group(3)

            if check_int(chapter):
                newInt = int(chapter)
            else:
                try:
                    newInt = roman.fromRoman(chapter.upper())
                except:
                    print("no roman", res.group(0), line)

            if book not in books.conv:
                print(res.group(1))

            line = line.replace(res.group(0), "[" + books.conv[book] + ". " + newInt.__str__(
            ) + ", " + verse.strip() + "](https://vulgata.online/bible/" + books.conv[book] + "." + newInt.__str__() + "?ed=DR2&vfn=DR2." + books.conv[book] + "." + newInt.__str__() + "."+verse.strip()+":vs)")

            res = regexp.search(line)

        lines[count] = line
        count = count + 1

        # if count >= 200:
        #     break
        # else:
        #     count = count + 1

    with open("./_scripts/AquinasLent/full3.md", "w", encoding="utf-8") as file:
        file.writelines(lines)
