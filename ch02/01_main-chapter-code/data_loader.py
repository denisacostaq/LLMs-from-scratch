from torch.utils.data import DataLoader

from gpt_dataset_v1 import GPTDatasetV1

import tiktoken

def create_dataloader_v1(txt, batch_size=4, max_length=256, stride=128, shuffle=True, drop_last=True, num_workers=0):
    tokenizer = tiktoken.get_encoding("gpt2")
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers, drop_last=drop_last)
    return dataloader

with open("the-verdict.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

dataloader = create_dataloader_v1(txt=raw_text, batch_size=1, max_length=4, stride=1, shuffle=False)
data_iterator = iter(dataloader)
first_batch = next(data_iterator)
print(first_batch)