#!/bin/env python3

import os

filename = os.path.join("news", "who_en.txt")
with open(filename, "r", encoding='utf-8') as f:
    lines_already_in_file = f.read()
write_mode = "w"
lines = lines_already_in_file.split('\n')
lines_to_append = ""
lines_removed = 0
print(str(len(lines)))
for line in lines:
    if "WHO" in line or "World Health Organization" in line:
        lines_to_append += line
        lines_to_append += "\n"
    else:
        lines.remove(line)
        lines_removed += 1

print(str(lines_removed))
with open(filename, write_mode, encoding='utf-8') as f:
    f.write(lines_to_append)