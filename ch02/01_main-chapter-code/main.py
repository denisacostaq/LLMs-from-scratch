import re

with open("the-verdict.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()
print("Total number of character:", len(raw_text))
print(raw_text[:99])
split_text = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
striped_tokens = [item for item in split_text if item.strip()]
print(striped_tokens)