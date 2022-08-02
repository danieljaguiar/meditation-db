from datetime import datetime
from io import TextIOWrapper
import os
import json
from string import Template
from tokenize import String


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

                language_updated = False

                for language_count in tag_from_list["counts"]:
                    language_index = language_index + 1

                    if language_count["language"] == language:
                        # Tag from meditation was found already in the tag list
                        new_tag_list[tag_list_index]["counts"][language_index]["count"] = new_tag_list[
                            tag_list_index]["counts"][language_index]["count"] + 1
                        language_updated = True

                if language_updated == False:
                    # We have a tag, but no count for this language
                    new_tag_list[tag_list_index]["counts"].append(
                        {"language": language, "count": 1})

        if tag_updated == False:
            new_tag_list.append({"name": tag_from_meditation, "counts": [{
                                "language": language, "count": 1}]})

        #         if not tag_from_list["count"]:
        #             tag_from_list["name"]["count"] = [{"language": language, "count": 1}]
        #             tag_updated = True

        # tag_in_new_list = [
        #     item for item in new_tag_list if item["name"] == tag_from_meditation]

        # if tag_in_new_list and len(tag_in_new_list) >= 1:
        #     temp_tag = tag_in_new_list[0]

        #     language_count = [
        #         lcount for lcount in temp_tag["languageCount"] if lcount["language"] == language]

        #     if language_count and len(language_count) >= 1:

        #         temp_count = language_count[0]

        #         temp_count = {"language": language,
        #                       "count": temp_count["count"] + 1}
        #     else:
        #         temp_tag["languageCount"].append(
        #             {"language": language, "count": 1})

        # else:
        #     new_tag_list.append({"name": tag_from_meditation, "languageCount": [{
        #                         "language": language, "count": 1}]})


print(new_tag_list)

output_path = "./_index/tags.json"

try:
    os.remove(output_path)
except OSError:
    pass


with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(new_tag_list, f, ensure_ascii=False, indent=4)
