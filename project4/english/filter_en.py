import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(BASE_DIR, "words_alpha.txt")
output_file = os.path.join(BASE_DIR, "words_5_8_utf8.txt")

min_len = 5
max_len = 8

seen = set()

with open(input_file, "r", encoding="utf-8") as f_in, \
     open(output_file, "w", encoding="utf-8") as f_out:

    for line in f_in:
        word = line.strip().lower()

        # only letters
        if not re.fullmatch(r"[a-z]+", word):
            continue

        # lenght 5–8
        if not (min_len <= len(word) <= max_len):
            continue
        if word in seen:
            continue
        seen.add(word)

        f_out.write(word + "\n")

print("ready:", len(seen))