# Import the modules we need
import sys

# This is the main file for the bookbot program. It will analyze a book and return some statistics about it.
def main():
    print(f"============ BOOKBOT ============ \n Analyzing book found at {path_to_file}")
    print(f"---------- Word Count ---------- \n Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in sorted_letters:
        print(f"{letter}: {sorted_letters[letter]}")
    print("============= END ===============")


# Save a reference to the filepath of the book we're analyzing.
path_to_file = sys.argv[1] if len(sys.argv) > 1 else print("Usage: python3 main.py <path_to_book>") and sys.exit(1)
# "/home/natehawke/bookbot/books/frankenstein.txt"
    
# Get the text of the book and return it.
def get_book_text(filepath): 
    if filepath == None:
        file_contents = "No file found"
        #print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        with open(filepath) as f:
            file_contents = f.read()
            #print(file_contents)
    return file_contents

# Save a reference to the text of the book.
contents = get_book_text(path_to_file)

from stats import get_word_count
# Get the word count out of the text by splitting it into a list of words.
word_count = get_word_count(contents)

from stats import sort_letter_count
# Sort the dictionary by value in descending order
sorted_letters = sort_letter_count(contents)

main()
