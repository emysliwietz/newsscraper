#!/bin/env python3

import requests
from bs4 import BeautifulSoup
import os

# Name of file, Url to get data from
urls = [
    ('corona_maßnahmen_de.txt', 'https://news.google.com/search?q=corona%20ma%C3%9Fnahmen&hl=de&gl=DE&ceid=DE%3Ade'),
    ('corona_measures_en.txt', 'https://news.google.com/search?q=corona%20measures&hl=en-GB&gl=GB&ceid=GB%3Aen'),
    ('corona_maatregelen_nl.txt', 'https://news.google.com/search?q=corona%20maatregelen&hl=nl&gl=NL&ceid=NL%3Anl'),
    ('who_de.txt', 'https://news.google.com/search?q=who&hl=de&gl=DE&ceid=DE%3Ade'),
    ('who_en.txt', 'https://news.google.com/search?q=who&hl=en-GB&gl=GB&ceid=GB%3Aen'),
    ('who_nl.txt', 'https://news.google.com/search?q=who&hl=nl&gl=NL&ceid=NL%3Anl'),
    ('donald_trump_de.txt', 'https://news.google.com/search?q=donald%20trump&hl=de&gl=DE&ceid=DE%3Ade'),
    ('donald_trump_en.txt', 'https://news.google.com/search?q=donald%20trump&hl=en-GB&gl=GB&ceid=GB%3Aen'),
    ('donald_trump_nl.txt', 'https://news.google.com/search?q=donald%20trump&hl=nl&gl=NL&ceid=NL%3Anl'),
    ('eu_de.txt', 'https://news.google.com/search?q=eu&hl=de&gl=DE&ceid=DE%3Ade'),
    ('eu_en.txt', 'https://news.google.com/search?q=eu&hl=en-GB&gl=GB&ceid=GB%3Aen'),
    ('eu_nl.txt', 'https://news.google.com/search?q=eu&hl=nl&gl=NL&ceid=NL%3Anl'),
    ('italien_de.txt', 'https://news.google.com/search?q=italien&hl=de&gl=DE&ceid=DE%3Ade'),
    ('italy_en.txt', 'https://news.google.com/search?q=italy&hl=en-GB&gl=GB&ceid=GB%3Aen'),
    ('italie_nl.txt', 'https://news.google.com/search?q=italie&hl=nl&gl=NL&ceid=NL%3Anl'),
    ('corona_maskenpflicht_de.txt', 'https://news.google.com/search?q=corona%20maskenpflicht&hl=de&gl=DE&ceid=DE%3Ade'),
    ('corona_mask_requirement.txt', 'https://news.google.com/search?q=corona%20mask%20requirement&hl=en-GB&gl=GB&ceid=GB%3Aen'),
    ('corona_masker_nl.txt', 'https://news.google.com/search?q=corona%20masker&hl=nl&gl=NL&ceid=NL%3Anl'),
    ('corona_tracking_app_de.txt', 'https://news.google.com/search?q=corona%20tracking%20app&hl=de&gl=DE&ceid=DE%3Ade'),
    ('corona_tracking_app_en.txt', 'https://news.google.com/search?q=corona%20tracking%20app&hl=en-GB&gl=GB&ceid=GB%3Aen'),
    ('corona_tracking_app_nl.txt', 'https://news.google.com/search?q=corona%20tracking%20app&hl=nl&gl=NL&ceid=NL%3Anl'),
    ('corona_lockerung_de.txt', 'https://news.google.com/search?q=corona%20lockerung&hl=de&gl=DE&ceid=DE%3Ade'),
    ('corona_relaxation_en.txt', 'https://news.google.com/search?q=corona%20relaxation&hl=en-GB&gl=GB&ceid=GB%3Aen'),
    ('corona_versoepeling_nl.txt', 'https://news.google.com/search?q=corona%20versoepeling&hl=nl&gl=NL&ceid=NL%3Anl'),
    ('schlagzeilen_de.txt', 'https://news.google.com/topstories?hl=de&gl=DE&ceid=DE:de'),
    ('headlines_en.txt', 'https://news.google.com/topstories?hl=en-GB&gl=GB&ceid=GB:en'),
    ('artikelkoppen_nl.txt', 'https://news.google.com/topstories?hl=nl&gl=NL&ceid=NL:nl')
]

if not os.path.exists("news"):
    os.mkdir("news")

for (filename, url) in urls:
    filename = os.path.join("news", filename)
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
    i = 0
    for (title, source, timestamp) in articles:
        i += 1
        line = "{} | {} | {}\n".format(title.text, source.text, timestamp['datetime'])
        if line not in lines_already_in_file:
            lines_to_append += line
        if i > 24:
            break

    with open(filename, write_mode, encoding='utf-8') as f:
        f.write(lines_to_append)
    print("Finished updating {}".format(filename))

