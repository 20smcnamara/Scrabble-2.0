import time
from itertools import permutations


def read_words():
    to_return = []
    file_object = open("words", "r")
    string = file_object.read()
    for word in string.split("\n"):
        to_return.append(word)
    return to_return


def fastest_search(letters):
    mixes = find_all_mixes_perm(letters)
    good = []
    for x in mixes:
        if x in words:
            good.append(x)
    best = [0, "-1"]
    for word in good:
        points = 0
        for letter in word:
            points += LETTER_VALUES[letter]
        if best[0] < points:
            best = [points, word]
    return best[1]


def find_all_mixes_perm(strings):
    remade_string = ""
    mixes = []
    for letter in strings:
        remade_string += letter
    for x in range(len(strings) - 1):
        for y in range(len(strings)):
            new_strings = []
            for i in range(x + 1):
                new_strings.append(strings[:i] + strings[i + 1:])
            newest_strings = []
            for string in new_strings:
                made_string = ""
                for letter in string:
                    made_string += letter
                newest_strings.append(made_string)
            for i in newest_strings:
                mixes.append(set([''.join(p) for p in permutations(i)]))
    return mixes


words = read_words()
LETTER_VALUES = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3,
                 "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4,
                 "Z": 10}
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
init_time = time.time()
# print(fastest_search(["A", "B", "C", "K"]))
# print(find_all_mixes_perm(["A", "B", "C", "D"]))

w = "Test"
to_perm = []
for num_skips in range(1, len(w)):
    for skip_start_index in range(len(w)):
        restart_index = skip_start_index + num_skips
        start_index = 0
        if restart_index == len(w):
            start_index = restart_index - len(w)
        to_perm.append(w[start_index:skip_start_index] + w[skip_start_index + num_skips:restart_index])
        print(num_skips, ": ", start_index, "|", restart_index)  # w[start_index:skip_start_index] + "|" + w[skip_start_index + num_skips:restart_index])
print(to_perm)
