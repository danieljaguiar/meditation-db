from pymongo import MongoClient
from pathlib import Path
import requests
import re
import codecs
import json
import datetime
import os
import json

f = open('./_scripts/AscanioBreviario/footnotes.json', encoding="utf-8")

# returns JSON object as
# a dictionary
allFootnotes = json.load(f)

initial_path = "./books-content/breviario-confianca/"


def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.


count = 0

full_file_paths = get_filepaths(initial_path)

regexp = re.compile(r'\(#BOOKMARK ([0-9]{1,3})\#\)')

for file_path in full_file_paths:
    # if count >= 30:
    #     break
    # else:
    #     count = count + 1

    with open(file_path, encoding="utf-8") as file:
        footnotes_lines = "\n"
        footnotes_ref = 1
        lines = file.readlines()
        lineCount = 0

        for line in lines:
            res = regexp.search(line)

            while res:
                value = [x for x in allFootnotes if x["bookmark"]
                         == int(res.group(1))]

                if value[0]["type"] == "inPlace":
                    line = line.replace(
                        res.group(0), " (" + value[0]["text"].strip()+")")

                if value[0]["type"] == "bottom":
                    line = line.replace(
                        res.group(0), " [^" + footnotes_ref.__str__()+"]")

                    footnotes_lines = footnotes_lines + \
                        "\n[^" + footnotes_ref.__str__() + "]: " + \
                        value[0]["text"].strip()

                    footnotes_ref = footnotes_ref + 1

                res = regexp.search(line)

            lines[lineCount] = line

            lineCount = lineCount + 1

    # print(lines)
    # print(footnotes_lines)

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)
        if footnotes_ref >= 2:
            file.writelines(footnotes_lines)
