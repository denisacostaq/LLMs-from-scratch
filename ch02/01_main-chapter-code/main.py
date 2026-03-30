import re

with open("the-verdict.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()
print("Total number of character:", len(raw_text))
print(raw_text[:99])
split_text = re.split(r'(\s)', raw_text)
print(split_text)