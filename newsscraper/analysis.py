#!/bin/env python3

import requests
from bs4 import BeautifulSoup
import os

# Names of files
files_de = [
    ('corona_maßnahmen_de.txt'),
    ('who_de.txt'),
    ('donald_trump_de.txt'),
    ('eu_de.txt'),
    ('italien_de.txt'),
    ('corona_maskenpflicht_de.txt'),
    ('corona_tracking_app_de.txt'),
    ('corona_lockerung_de.txt'),
    ('schlagzeilen_de.txt')
]

files_en = [
    ('corona_measures_en.txt'),
    ('who_en.txt'),
    ('donald_trump_en.txt'),
    ('eu_en.txt'),
    ('italy_en.txt'),
    ('corona_mask_requirement.txt'),
    ('corona_tracking_app_en.txt'),
    ('corona_relaxation_en.txt'),
    ('headlines_en.txt')
]

files_nl =[
    ('corona_maatregelen_nl.txt'),
    ('who_nl.txt'),
    ('donald_trump_nl.txt'),
    ('eu_nl.txt'),
    ('italie_nl.txt'),
    ('corona_masker_nl.txt'),
    ('corona_tracking_app_nl.txt'),
    ('corona_versoepeling_nl.txt'),
    ('artikelkoppen_nl.txt')
]

files = [
    ('corona_maßnahmen_de.txt'),
    ('who_de.txt'),
    ('donald_trump_de.txt'),
    ('eu_de.txt'),
    ('italien_de.txt'),
    ('corona_maskenpflicht_de.txt'),
    ('corona_tracking_app_de.txt'),
    ('corona_lockerung_de.txt'),
    ('schlagzeilen_de.txt'),
    ('corona_measures_en.txt'),
    ('who_en.txt'),
    ('donald_trump_en.txt'),
    ('eu_en.txt'),
    ('italy_en.txt'),
    ('corona_mask_requirement.txt'),
    ('corona_tracking_app_en.txt'),
    ('corona_relaxation_en.txt'),
    ('headlines_en.txt'),
    ('corona_maatregelen_nl.txt'),
    ('who_nl.txt'),
    ('donald_trump_nl.txt'),
    ('eu_nl.txt'),
    ('italie_nl.txt'),
    ('corona_masker_nl.txt'),
    ('corona_tracking_app_nl.txt'),
    ('corona_versoepeling_nl.txt'),
    ('artikelkoppen_nl.txt')
]

if not os.path.exists("analysis"):
    os.mkdir("analysis")


def source_count():
    for file in files:
        filename = file.replace('.txt', '')
        filepath = os.path.join("analysis", filename + "_source_count.txt")
        if os.path.exists(filepath):
            os.remove(filepath)

        write_mode = "w"  # Append to file
        original_path = os.path.join("news", file)
        with open(original_path, "r", encoding='utf-8') as f:
            lines_in_file = f.read()

        lines = lines_in_file.split("\n")
        sources = []
        occurences = []
        for line in lines:
            if line == '':
                break
            line_elements = line.split(' | ')
            source_index = len(line_elements) - 2
            source = line_elements[source_index]
            if source not in sources:
                sources.append(source)
                occurences.append(1)
            else:
                index = sources.index(source)
                occurences[index] += 1

        num_sources = len(sources) - 1
        lines_to_append = ""
        for i in range(num_sources):
            line = "{}: {}\n".format(sources[i], occurences[i])
            lines_to_append += line

        with open(filepath, write_mode, encoding='utf-8') as f:
            f.write(lines_to_append)

        print("Finished analysing " + file)


source_count()
