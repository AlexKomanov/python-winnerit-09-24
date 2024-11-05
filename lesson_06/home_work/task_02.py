from typing import List

def filter_words(words: List[str], min_length: int) -> List[str]:
    return [word for word in words if len(word) >= min_length]


words_list = ["apple", "banana", "cherry", "date", "fig", "grape"]
filtered_words = filter_words(words_list, 5)
print(filtered_words)
