from datetime import datetime
from io import TextIOWrapper
import os
import json
from string import Template
from tokenize import String

topics_translations = open(
    './_index/topics_translations.json', encoding="utf-8")
localizations = json.load(topics_translations)

books_file = open('./_index/books.json', encoding="utf-8")
books = json.load(books_file)

meditations_file = open('./_index/meditations.json', encoding="utf-8")
meditations = json.load(meditations_file)

new_tag_list = []


for meditation in meditations:
    book_from_meditation = [
        book for book in books if books if book["id"] == meditation["bookId"]]

    language = book_from_meditation[0]["language"]

    for tag_from_meditation in meditation["topics"]:
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

                language_updated = False

                for language_count in tag_from_list["languageCount"]:
                    language_index = language_index + 1

                    if language_count["key"] == language:
                        # Tag from meditation was found already in the tag list
                        new_tag_list[tag_list_index]["languageCount"][language_index]["count"] = new_tag_list[
                            tag_list_index]["languageCount"][language_index]["count"] + 1
                        language_updated = True

                if language_updated == False:
                    # We have a tag, but no count for this language
                    new_tag_list[tag_list_index]["languageCount"].append(
                        {"key": language, "count": 1})

                book_index = -1
                book_updated = False

                for book_count in tag_from_list["bookCount"]:
                    book_index = book_index + 1

                    if book_count["key"] == meditation["bookId"]:
                        # Tag from meditation was found already in the tag list
                        new_tag_list[tag_list_index]["bookCount"][book_index]["count"] = new_tag_list[
                            tag_list_index]["bookCount"][book_index]["count"] + 1
                        book_updated = True

                if book_updated == False:
                    # We have a tag, but no count for this book
                    new_tag_list[tag_list_index]["bookCount"].append(
                        {"key": meditation["bookId"], "count": 1})

        if tag_updated == False:
            loc_array = [
                loc for loc in localizations if loc if loc["name"] == tag_from_meditation]

            loc_for_newentry = []

            if loc_array and len(loc_array) > 0:
                loc = loc_array[0]
                loc_for_newentry.append(
                    {"key": "en", "title": loc["title_en"], "description": loc["desc_en"]})
                loc_for_newentry.append(
                    {"key": "pt", "title": loc["title_pt"], "description": loc["desc_pt"]})

            new_tag_list.append({
                "name": tag_from_meditation,
                "bookCount": [
                    {"key": meditation["bookId"], "count": 1}
                ],
                "languageCount": [{"key": language, "count": 1}], "localization": loc_for_newentry})


output_path = "./_index/topics.json"

try:
    os.remove(output_path)
except OSError:
    pass


with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(new_tag_list, f, ensure_ascii=False, indent=4)
