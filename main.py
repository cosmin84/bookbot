def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_contents(book_path)
    words_count = get_words_count(contents)
    chars_count = get_chars_count(contents)
    
    processed_chars = process_chars_dictionary(chars_count)
    processed_chars.sort(reverse=True, key=sort_on)
    show_report(book_path, words_count, processed_chars)

def show_report(book_path, words_count, processed_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print("\n")

    for item in processed_chars:
        print(f"The '{item["char"]}' character was found {item["num"]} times")

def sort_on(dict):
    return dict["num"]

def process_chars_dictionary(chars):
    new = []

    for key, value in chars.items():
        if key.isalpha():
            new.append({
                "char": key,
                "num": value
            })
    
    return new

def get_words_count(contents):
    words = contents.split()
    return len(words)


def get_chars_count(contents):
    chars = {}
    for c in contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_contents(path):
    with open(path) as f:
        return f.read()


main()
