import random

WORD_LENGTH = 7

# Sort words into groups of word length
def sort_words(words):
    sorted_words = {}
    for word in words:
        length = len(word)
        if length not in sorted_words.keys():
            sorted_words[length] = []
        sorted_words[length].append(word)
    return sorted_words

# Create a frequency table for the probabliliy for specific letter
# to be in a certain position of a word of a certain length
def create_frequency_table(word_list, char_pos):
    char_counts = {}
    for word in word_list:
        char = word[char_pos]
        if char not in char_counts.keys():
            char_counts[char] = 0
        char_counts[char] += 1
    total = sum(char_counts.values())
    frequency_table = {}
    running_total = 0
    for char in char_counts.keys():
        running_total += char_counts[char] / total
        frequency_table[char] = running_total
    return frequency_table

def check_frequency_table(f_table, value):
    for char in f_table.keys():
        if value < f_table[char]:
            return char
    # Just return the last char. Only here due to floating point inaccuracies
    return char 

def main():
    # Get list of words
    with open('wlist_match10.txt') as file:
        words = file.read().split('\n')
        words.remove('')
    sorted_words = sort_words(words)
    # Create frequency tables
    frequencies = {}
    for length in sorted_words.keys(): 
        frequencies[length] = []
        for char_pos in range(length):
            frequencies[length].append(
                create_frequency_table(sorted_words[length], char_pos)
            )
    # Generate a new word
    for f_table in frequencies[7]:
        # Predict character
        print(check_frequency_table(f_table, random.random()), end='')
    print()

if __name__ == '__main__':
    main()
