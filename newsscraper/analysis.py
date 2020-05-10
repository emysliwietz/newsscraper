#!/bin/env python3

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

if not os.path.exists("analysis/source_count"):
    os.mkdir("analysis/source_count")

if not os.path.exists("analysis/date_count"):
    os.mkdir("analysis/date_count")


def sort_lines(lines):
    lines_split = lines.split("\n")
    lines_list = []
    lines_for_file = ""
    for line in lines_split:
        if line == '':
            break

        numbers = line.split(": ")
        lines_list.append((numbers[0], int(numbers[1])))

    lines_list.sort(key=lambda x:x[1], reverse=True)
    length = len(lines_list) - 1
    for i in range(length):
        line = "{}: {}\n".format(lines_list[i][0], lines_list[i][1])
        lines_for_file += line

    return lines_for_file


def calculate_percentages(lines, total_headlines):
    lines_split = lines.split("\n")
    percentages = []
    lines_for_file = ""
    for line in lines_split:
        if line == '':
            break

        index = lines.index(line)
        numbers = line.split(": ")
        num = int(numbers[1])
        percentages.append(num/total_headlines * 100)

    length = len(lines_split) - 1
    for i in range(length):
        line = "{} ({}%)\n".format(lines_split[i], str(percentages[i]))
        lines_for_file += line

    return lines_for_file


def get_sources_and_occurences(lines, sources, occurences):
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

    return sources, occurences


def perform_source_analysis(file, sources, occurences, total_headlines):
    original_path = os.path.join("news", file)
    with open(original_path, "r", encoding='utf-8') as f:
        lines_in_file = f.read()

    lines = lines_in_file.split("\n")
    total_headlines += len(lines)
    sources, occurences = get_sources_and_occurences(lines, sources, occurences)
    return sources, occurences, total_headlines, lines


def write_to_file(sources, occurences, filepath, write_mode, lines):
    num_sources = len(sources) - 1
    lines_to_sort = ""
    for i in range(num_sources):
        line = "{}: {}\n".format(sources[i], occurences[i])
        lines_to_sort += line

    lines_to_append = sort_lines(lines_to_sort)
    lines_to_append = calculate_percentages(lines_to_append, len(lines) - 1)
    with open(filepath, write_mode, encoding='utf-8') as f:
        f.write(lines_to_append)


def source_count_per_file():
    for file in files:
        filename = file.replace('.txt', '')
        filepath = os.path.join("analysis/source_count", filename + "_source_count.txt")
        if os.path.exists(filepath):
            os.remove(filepath)

        write_mode = "w"  # Append to file
        original_path = os.path.join("news", file)
        with open(original_path, "r", encoding='utf-8') as f:
            lines_in_file = f.read()

        lines = lines_in_file.split("\n")
        sources = []
        occurences = []
        print("Total number of headlines: " + str(len(lines) - 1))
        sources, occurences = get_sources_and_occurences(lines, sources, occurences)
        write_to_file(sources, occurences, filepath, write_mode, lines)

        print("Finished analysing " + file)


def source_count_de():
    sources = []
    occurences = []
    total_headlines = 0
    filepath = os.path.join("analysis/source_count", "source_count_de.txt")
    if os.path.exists(filepath):
        os.remove(filepath)

    write_mode = "w"  # Append to file
    for file in files_de:
        sources, occurences, total_headlines, lines = perform_source_analysis(file, sources, occurences, total_headlines)

    print("Total number of headlines: " + str(total_headlines - 1))
    write_to_file(sources, occurences, filepath, write_mode, lines)

    print("Finished analysing German files")


def source_count_en():
    sources = []
    occurences = []
    total_headlines = 0
    filepath = os.path.join("analysis/source_count", "source_count_en.txt")
    if os.path.exists(filepath):
        os.remove(filepath)

    write_mode = "w"  # Append to file
    for file in files_en:
        sources, occurences, total_headlines, lines = perform_source_analysis(file, sources, occurences, total_headlines)

    print("Total number of headlines: " + str(total_headlines - 1))
    write_to_file(sources, occurences, filepath, write_mode, lines)

    print("Finished analysing English files")


def source_count_nl():
    sources = []
    occurences = []
    total_headlines = 0
    filepath = os.path.join("analysis/source_count", "source_count_nl.txt")
    if os.path.exists(filepath):
        os.remove(filepath)

    write_mode = "w"  # Append to file
    for file in files_nl:
        sources, occurences, total_headlines, lines = perform_source_analysis(file, sources, occurences, total_headlines)

    print("Total number of headlines: " + str(total_headlines - 1))
    write_to_file(sources, occurences, filepath, write_mode, lines)

    print("Finished analysing Dutch files")


def source_count():
    source_count_per_file()
    source_count_de()
    source_count_en()
    source_count_nl()


def date_count():
    for file in files:
        filename = file.replace('.txt', '')
        filepath = os.path.join("analysis/date_count", filename + "_date_count.txt")
        if os.path.exists(filepath):
            os.remove(filepath)

        write_mode = "w"  # Append to file
        original_path = os.path.join("news", file)
        with open(original_path, "r", encoding='utf-8') as f:
            lines_in_file = f.read()

        lines = lines_in_file.split("\n")
        dates = []
        occurences = []
        for line in lines:
            if line == '':
                break

            line_elements = line.split(' | ')
            time_index = len(line_elements) - 1
            time_elements = line_elements[time_index].split('T')
            date = time_elements[0]
            if date not in dates:
                dates.append(date)
                occurences.append(1)
            else:
                index = dates.index(date)
                occurences[index] += 1

        write_to_file(dates, occurences, filepath, write_mode, lines)

        print("Finished analysing dates in " + file)


source_count()
date_count()
