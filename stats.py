# Get the word count out of the text by splitting it into a list of words.
def get_word_count(content):
    words_in_content = content.split()
    l_wordcount = 0
    # Loop over the words and increment the word count for each word.
    for word in words_in_content:
        l_wordcount += 1
    return l_wordcount

# Count the number of characters in the content
def count_letters(content):
    # Convert the content to lowercase to ensure case-insensitive counting
    lowercase_content = content.lower()
    # Create a dictionary to store character counts
    letter_count = {}
    # Iterate over each character in the content
    for letter in lowercase_content:
        if letter.isalpha():  # Check if the character is a letter
            letter_count[letter] = letter_count.get(letter, 0) + 1
    # Return the dictionary with character counts
    return letter_count

def sort_letter_count(content):
    letters_in_content = count_letters(content)
    # Sort the dictionary by value in descending order
    sorted_letter_count = dict(sorted(letters_in_content.items(), key=lambda item: item[1], reverse=True))
    # Return the sorted dictionary
    return sorted_letter_count