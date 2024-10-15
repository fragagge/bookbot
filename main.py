def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    char_dict = count_characters(text)
    report_list = dict_to_sorted_list(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print()

    for item in report_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def sort_on(d):
    return d["num"]    
    
def dict_to_sorted_list(num_char_dict):
    sorted_list = []
    for num_char in num_char_dict:
        sorted_list.append({"char": num_char, "num": num_char_dict[num_char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def count_characters(text):
    lower_text = text.lower()
    characters = {}
    for char in lower_text:
        characters[char] = characters.get(char, 0) + 1
    return characters


def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

    


main()