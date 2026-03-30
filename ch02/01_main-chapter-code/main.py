import re
from simple_tokenizer_v2 import SimpleTokenizerV2

with open("the-verdict.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()
print("Total number of character:", len(raw_text))
print(raw_text[:99])
split_text = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
striped_tokens = [item for item in split_text if item.strip()]
print(striped_tokens)

all_words = sorted(set(striped_tokens))
all_words.extend(["<|endoftext|>", "<|unk|>"])
vocab_size = len(all_words)
print("Vocabulary size:", vocab_size)

vocab = {word: index for index, word in enumerate(all_words)}
for i, item in enumerate(all_words[:50]):
    print(f"{item}: {i:3d}")


tokenizer = SimpleTokenizerV2(vocab)
text = """
"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."
"""
ids = tokenizer.encode(text)
print(ids)
decoded = tokenizer.decode(ids)
print(decoded)

text = "Hello, do you like tea?"
print(tokenizer.encode(text))

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))
print(text)

print(tokenizer.encode(text))
print(tokenizer.decode(tokenizer.encode(text)))