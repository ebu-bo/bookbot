def main():
    file_path = "./books/frankenstein.txt"
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    char_count = get_num_count(book_text)
    #sorted_true = sort_in(char_count)
    print(f"{num_words} words found in the document")
    print(char_count)
    #print("============ BOOKBOT ============")
    #print(f"Analyzing book found at {file_path}...")
    #print("----------- Word Count ----------")
    #print(f"Found {num_words} total words")
    #print("--------- Character Count -------")
    #print(f"{sorted_true}") # dictionary to be finished
    #print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

from stats import get_num_words
from stats import get_num_count
#from stats import sort_in

main()