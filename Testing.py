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
    mixes = find_all_mixes_perm_but_better(letters)
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
    return sort_letters(best)


words = read_words()
LETTER_VALUES = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3,
                 "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4,
                 "Z": 10}
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
init_time = time.time()


def find_all_mixes_perm_but_better(strings):
    remade_string = ""
    uncollated_mixes = []
    mixes = []
    to_perm = []
    for letter in strings:
        remade_string += letter
    for num_skips in range(1, len(remade_string) - 1):
        for skip_start_index in range(len(remade_string) - 1):
            for begin_index in range(num_skips):
                print(remade_string[begin_index:skip_start_index] + "|" + remade_string[skip_start_index +
                                                                                        1:len(remade_string)])
                # to_perm.append(remade_string[0:skip_start_index] + remade_string[skip_start_index +
                #                                                                       1:len(remade_string)])
    print(to_perm)
    to_perm.append(remade_string)
    for i in to_perm:
        if len(i) > 1:
            uncollated_mixes.append(set([''.join(p) for p in permutations(i)]))
    for i in uncollated_mixes:
        for x in i:
            mixes.append(x)
    return mixes


#print("\n", find_all_mixes_perm_but_better(["A", "B", "C", "D"]))
word = "ABCD"
print(word[0:1] + "|" + word[2:4])

# 1
#   0
#       0,1     1,3
#       0,1     2,4
#   1
#       1,2     2,4

# 2
#   0
#       0,1     1,2
#       0,1     2,3
#       0,1     3,4
#   1
#       1,2     2,3
#       1,2     3,4
#   2
#       2,3     3,4

for num_skip in range(1, len(word) - 1):
    for start_index in range(num_skip + 2):
        for end_index in range(start_index + 1, len(word) - 1):
            print(start_index, end_index)
            print(word[start_index:start_index + 1] + "|" + word[end_index: end_index + len(word) - 2 + num_skip])
    print("")
