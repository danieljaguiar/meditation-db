from datetime import datetime
from io import TextIOWrapper
import os
import json
from string import Template
from tokenize import String


meditations_file = open('./_index/meditations.json', encoding="utf-8")

meditations = json.load(meditations_file)

tag_list = []


for meditation in meditations:

    for tag in meditation["tags"]:
        if tag == "":
            continue

        tag_in_list = [item for item in tag_list if item["name"] == tag]

        if tag_in_list and len(tag_in_list) >= 1:
            first_tag = tag_in_list[0]
            first_tag["count"] = first_tag["count"] + 1
        else:
            tag_list.append({"name": tag, "count": 1})


print(tag_list)

output_path = "./_index/tags.json"

try:
    os.remove(output_path)
except OSError:
    pass


with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(tag_list, f, ensure_ascii=False, indent=4)
