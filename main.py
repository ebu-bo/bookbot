def main():
    file_path = "./books/frankenstein.txt"
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def get_num_words(book_text):
    contents_split = book_text.split()
    return len(contents_split)

main()