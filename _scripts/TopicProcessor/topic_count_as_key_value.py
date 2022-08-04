from datetime import datetime
from io import TextIOWrapper
import os
import json
from string import Template
from tokenize import String

tags_translations = open('./_index/tags_translations.json', encoding="utf-8")
localizations = json.load(tags_translations)


books_file = open('./_index/books.json', encoding="utf-8")
books = json.load(books_file)

meditations_file = open('./_index/meditations.json', encoding="utf-8")
meditations = json.load(meditations_file)

new_tag_list = []


for meditation in meditations:
    book_from_meditation = [
        book for book in books if books if book["id"] == meditation["bookId"]]

    language = book_from_meditation[0]["language"]

    for tag_from_meditation in meditation["tags"]:
        # print("-------------------------------------")
        # print(new_tag_list)
        if tag_from_meditation == "":
            continue

        tag_list_index = -1
        tag_updated = False

        for tag_from_list in new_tag_list:
            tag_list_index = tag_list_index + 1

            if tag_from_list["name"] == tag_from_meditation:
                # Tag from meditation was found already in the list

                language_index = -1

                tag_updated = True
                print(tag_from_list)

                if language in tag_from_list:
                    new_tag_list[tag_list_index][language] = new_tag_list[tag_list_index][language] + 1
                else:
                    new_tag_list[tag_list_index][language] = 1

        if tag_updated == False:
            loc_array = [
                loc for loc in localizations if loc if loc["name"] == tag_from_meditation]

            loc_for_newentry = []

            if loc_array and len(loc_array) > 0:
                loc = loc_array[0]
                loc_for_newentry.append(
                    {"language": "en", "title": loc["title_en"], "description": loc["desc_en"]})
                loc_for_newentry.append(
                    {"language": "pt", "title": loc["title_pt"], "description": loc["desc_pt"]})

            new_entry = {"name": tag_from_meditation,
                         "localization": loc_for_newentry}
            new_entry[language] = 1
            new_tag_list.append(new_entry)


output_path = "./_index/tags.json"

try:
    os.remove(output_path)
except OSError:
    pass


with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(new_tag_list, f, ensure_ascii=False, indent=4)
