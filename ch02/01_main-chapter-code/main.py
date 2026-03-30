import re

with open("the-verdict.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()
print("Total number of character:", len(raw_text))
print(raw_text[:99])
split_text = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
striped_tokens = [item for item in split_text if item.strip()]
print(striped_tokens)

all_words = sorted(set(striped_tokens))
vocab_size = len(all_words)
print("Vocabulary size:", vocab_size)

vocab = {word: index for index, word in enumerate(all_words)}
for i, item in enumerate(all_words[:50]):
    print(f"{item}: {i:3d}")