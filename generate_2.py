import random
import sys

letters = list("abcdefghijklmnopqrstuvwxyz'")

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
        tally_matrix = [[0] * 27 for _ in range(27)]
        for word in sorted_words[length]:
            # Replace the letters with their position in the alphabet
            word = [letters.index(char) for char in word]
            # Iterate through each letter and the next letter
            for a, b in zip(word[:-1], word[1:]):
                tally_matrix[a][b] += 1
        # Normalize matrix
        matrix = []
        for row in range(len(tally_matrix)):
            matrix.append([])
            max_value = sum(tally_matrix[row])
            # Prevent division by zero
            if max_value == 0:
                continue
            for column in range(len(tally_matrix)):
                matrix[row].append(tally_matrix[row][column] / max_value)
        matrices[length] = matrix
    return matrices

def calc_char_pos_probabilities(sorted_words):
    probabilities = {}
    for length in sorted_words.keys():
        pos_probabilities = {}
        for pos in range(length):
            values = [0] * 27
            for word in sorted_words[length]:
                for letter in word:
                    values[letters.index(letter)] += 1
            max_value = sum(values)
            # Normalize
            for i in range(len(values)):
                values[i] /= max_value
            pos_probabilities[pos] = values
        probabilities[length] = pos_probabilities
    return probabilities

def main():
    # Get words
    with open('wlist_match10.txt') as file:
        words = file.read().lower().split('\n')
        words.remove('')

    # Sort words into groups of word lengths
    sorted_words = sort_words(words)

    # Create matricies
    matrices = create_matrices(sorted_words)

    # Calculate the probabilty of each letter being in certain positions
    # of certain length words
    #char_pos_probabilities = calc_char_pos_probabilities(sorted_words)

    for _ in range(int(sys.argv[2])):
        # Create a new word
        length = int(sys.argv[1])
        letter = random.choice(letters)
        # Check to make sure that the starting letter actually has probabilities
        # for next letters
        while not any(matrices[length][letters.index(letter)]):
            letter = random.choice(letters)        
        print(letter, end='')
        for pos in range(1, length):
            #weights = [
            #    x * y for x, y in zip(
            #        matrices[length][letters.index(letter)],
            #        char_pos_probabilities[length][pos]
            #    )
            #]
            weights = matrices[length][letters.index(letter)]
            letter = random.choices(letters, weights=weights)[0]
            print(letter, end='')
        print()

if __name__ == '__main__':
    main()
