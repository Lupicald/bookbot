import sys
from stats import count_words, count_characters, sort_characters, get_book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    count_words(book_text)

    print("--------- Character Count -------")
    char_dict = count_characters(book_text)
    sorted_chars = sort_characters(char_dict)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()

