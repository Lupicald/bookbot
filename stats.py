def count_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def count_characters(text):
    text = text.lower()
    char_counts = {}
    for c in text:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    return char_counts

def sort_characters(char_dict):
    char_list = []
    for c, count in char_dict.items():
        if c.isalpha():
            char_list.append({"char": c, "num": count})

    def sort_on(item):
        return item["num"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
