
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)

    print(f"There are {num_words} words in the text")
    print(char_count)

def get_char_count(text):
    char_dict = {}
    text_lower = text.lower()
    for letter in text_lower:
        char_dict[letter] = char_dict.get(letter, 0) + 1

    return char_dict

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()