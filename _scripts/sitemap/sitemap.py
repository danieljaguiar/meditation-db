from datetime import datetime
from io import TextIOWrapper
import os
import json
from string import Template
from tokenize import String


mapLine = Template("""\t<url>
\t\t<loc>https://meditatione.online/$path</loc>
\t\t<lastmod>$time</lastmod>
\t</url>""")


def output(value: String, file: TextIOWrapper):
    # print(value)
    file.write(value)
    file.write("\n")


site_map_path = "./_scripts/sitemap/IndexMeditatione.xml"
try:
    os.remove(site_map_path)
except:
    pass

with open(site_map_path, "a", encoding="utf8") as site_map_file:

    authors_file = open('./_index/authors.json', encoding="utf-8")
    authors = json.load(authors_file)

    output("""<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">""", site_map_file)

    for author in authors:
        # English
        try:
            m_time_str = os.path.getmtime(
                './authors/' + author["id"] + "-en.md")
            m_time = datetime.fromtimestamp(m_time_str).strftime('%Y-%m-%d')
            output(mapLine.substitute(
                path=("authors/" + author["id"]), time=m_time), site_map_file)
        except:
            pass

        # Portuguese
        try:
            m_time_str = os.path.getmtime(
                './authors/' + author["id"] + "-pt.md")
            m_time = datetime.fromtimestamp(m_time_str).strftime('%Y-%m-%d')
            output(mapLine.substitute(
                path=("pt/authors/" + author["id"]), time=m_time), site_map_file)
        except:
            pass

    books_file = open('./_index/books.json', encoding="utf-8")
    books = json.load(books_file)

    for meditation in books:
        try:
            m_time_str = os.path.getmtime(
                './books-description/' + meditation["id"] + ".md")
            m_time = datetime.fromtimestamp(m_time_str).strftime('%Y-%m-%d')
            language = ""

            if meditation["language"] != "en":
                language = meditation["language"] + "/"

            output(mapLine.substitute(
                path=(language + "books/" + meditation["id"]), time=m_time), site_map_file)
        except:
            pass

    meditations_file = open('./_index/meditations.json', encoding="utf-8")
    meditations = json.load(meditations_file)

    count = 0

    for meditation in meditations:
        m_time_str = os.path.getmtime(
            './books-content/' + meditation["bookId"] + "/" + meditation["order"].__str__() + ".md")
        m_time = datetime.fromtimestamp(m_time_str).strftime('%Y-%m-%d')
        mdt_book = list(
            filter(lambda x: x["id"] == meditation["bookId"], books))

        language = mdt_book[0]["language"]

        if language != "en":
            language = mdt_book[0]["language"] + "/"
        else:
            language = ""

        output(mapLine.substitute(
            path=(language + "books/" + meditation["bookId"] + "/" + meditation["slug"]), time=m_time), site_map_file)

    output("""</urlset>""", site_map_file)
