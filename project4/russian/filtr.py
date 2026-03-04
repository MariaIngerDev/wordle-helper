import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

src =  os.path.join(BASE_DIR,"russian.txt")            
dst = os.path.join(BASE_DIR,"words_7_utf8.txt" )      # result
target_len = 7

seen = set()
with open(src, "r", encoding="cp1251", errors="ignore") as f_in, \
     open(dst, "w", encoding="utf-8", newline="\n") as f_out:
    for line in f_in:
        w = line.strip().lower()
        if not w:
            continue
        w = w.replace("ё", "е")
        # only russian letters
        if not re.fullmatch(r"[а-я]+", w):
            continue
        if len(w) != target_len:
            continue
        if w in seen:
            continue
        seen.add(w)
        f_out.write(w + "\n")

print("ready:", len(seen))