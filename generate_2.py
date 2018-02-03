import random
import sys

letters = list('abcdefghijklmnopqrstuvwxyz')

# Create a dict of words of certain lengths
def sort_words(words):
    sorted_words = {}
    for word in words:
        length = len(word)
        if length not in sorted_words.keys():
            sorted_words[length] = []
        sorted_words[length].append(word)
    return sorted_words

def create_matrices(sorted_words):
    matrices = {}
    for length in sorted_words.keys():
        tally_matrix = [[0] * 26] * 26
        for word in sorted_words[length]:
            # Replace the letters with their position in the alphabet
            word = [letters.index(char) for char in word]
            # Iterate through each letter and the next letter
            for a, b in zip(word[1:], word[:-1]):
                tally_matrix[a][b] += 1
        # Normalize matrix
        matrix = []
        for row in range(len(tally_matrix)):
            matrix.append([])
            max_value = sum(tally_matrix[row])
            for column in range(len(tally_matrix)):
                matrix[row].append(tally_matrix[row][column] / max_value)
        matrices[length] = matrix
    return matrices

def main():
    # Get words
    with open('wlist_match10.txt') as file:
        words = file.read().lower().split('\n')
        words.remove('')

    # Sort words into groups of word lengths
    sorted_words = sort_words(words)

    # Create matricies
    matrices = create_matrices(sorted_words)

    # Create a new word
    length = int(sys.argv[1])
    letter = random.choice(letters)
    for _ in range(length):
        print(letter, end='')
        letter = random.choices(letters, matrices[length][letter.index(letter)])[0]
    print()

if __name__ == '__main__':
    main()
