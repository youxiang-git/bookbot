
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    list_char_count = convert_to_dict_list(char_count)
    list_char_count.sort(reverse=True, key=sort_on)

    generate_report(num_words, list_char_count)


def generate_report(num_words, list_char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for count in list_char_count:
        print(f"The '{count['char']}' character was found {count['num']} times")
    print("--- End report ---")

def convert_to_dict_list(dict):
    list_of_dicts = []
    for key, value in dict.items():
        if key.isalpha():
            list_of_dicts.append({"char": key, "num": value})

    return list_of_dicts

def sort_on(dict):
    return dict["num"]

def sort_on(dict):
    return dict["num"]

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