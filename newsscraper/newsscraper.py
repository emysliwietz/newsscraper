#!/bin/env python3

import requests
from bs4 import BeautifulSoup
import os

# Name of file, Url to get data from
urls = [
    ('news_en.txt', 'https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en'),
    ('news_de.txt', 'https://news.google.com/topstories?hl=de-DE&gl=DE&ceid=DE:de'),
]


for (filename, url) in urls:
    if os.path.exists(filename):
        with open(filename, "r") as f:
            lines_already_in_file = f.read()
        write_mode = "a" # Append if file exists
    else:
        lines_already_in_file = ""
        write_mode = "w" # And create file (overwrite) if it does not

    lines_to_append = ""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    titles = soup.findAll("a", {"class": "DY5T1d"})
    sources = soup.findAll("a", {"class": "wEwyrc AVN2gc uQIVzc Sksgp"})
    timestamps = soup.findAll("time", {"class": "WW6dff uQIVzc Sksgp"})
    
    articles = zip(titles, sources, timestamps)
    for (title, source, timestamp) in articles:
        line = "{} | {} | {}\n".format(title.text, source.text, timestamp['datetime'])
        if line not in lines_already_in_file:
            lines_to_append += line

    with open(filename, write_mode) as f:
        f.write(lines_to_append)
    print("Finished updating {}".format(filename))

