# Title: Top K Frequent Numbers

"""
You are given a list of integers. Your task is to:
Count how many times each number appears.
Return the K most frequent numbers.
If two numbers have the same frequency, return the smaller number first.
The result should be a list of integers sorted by frequency (descending), then by value (ascending).
"""


import re
from typing import List

def unique_words_count(words: List[str]) -> List[int]:
    result = []

    for words_line in words:
        if not words_line:
            result.append(0)
        else:
            words_line = re.sub(r"[^\w\s']", "", words_line.lower())
            unique = set(words_line.split())
            result.append(len(unique))

    return result

texts = [
    "Hello, world! Hello again.",
    "Python is great; python is powerful.",
    "Data, data, data... I can't make bricks without clay.",
    ""
]
print(unique_words_count(texts))