import re


class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {index: word for word, index in vocab.items()}

    def encode(self, text):
        split_text = re.split(r'([,.?_!"()\']|--|\s)', text)
        striped_tokens = [item for item in split_text if item.strip()]
        ids = [self.str_to_int[token] for token in striped_tokens]
        return ids

    def decode(self, ids):
        text: str = " ".join([self.int_to_str[id] for id in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text