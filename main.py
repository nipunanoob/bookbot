# print("hello world")
def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        book = f.read()
    return book

def count_characters(text):
    char_dict = {} 
    for letter in text:
        letter = letter.lower()
        if letter not in char_dict:
            char_dict[letter] = 1
        else:
            char_dict[letter] += 1
    return char_dict

def sort_on(dict):
    return dict["occurence"]

def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    wordcount = count_words(book)
    print(f"--- Begin book report of {book_path} ---")
    print(f"{wordcount} words found in document")

    char_dict = count_characters(book)
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({"character": char, "occurence": char_dict[char]}) 
    char_list.sort(reverse=True, key=sort_on)    

    for dic in char_list:
        print(f"""The {dic["character"]} character was found {dic["occurence"]} times""")
main()