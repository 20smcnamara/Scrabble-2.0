import pygame
pygame.init()

display_width = 800
display_hight = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
BONUS_STRINGS = ["", "2x\nWS", "2x\nLS", "3x\nWS", "3x\nLS", "Mid"]
            #   Up     Down      Left    Right
directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

# The below board matches with a picture at
# https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwiukpWtt6ffAhXtlOAKHRfzAWkQjRx6BAgBEAU&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FScrabble&psig=AOvVaw20SSGA8_KK0jKP66a4O2It&ust=1545155611561682
#                      A  B  C  D  E  F  G  H  I  J  K  L  M  N  O
BOARD_TILE_BONUSES = [[3, 3, 3, 2, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 3],    # 1
                      [0, 1, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 1, 0],    # 2
                      [0, 0, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 1, 0, 0],    # 3
                      [2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2],    # 4
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],    # 5
                      [0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0],    # 6
                      [0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0],    # 7
                      [3, 0, 0, 1, 0, 0, 0, 5, 0, 0, 0, 1, 0, 0, 3],    # 8
                      [0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0],    # 9
                      [0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0],    # 10
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],    # 11
                      [2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2],    # 12
                      [0, 0, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 1, 0, 0],    # 13
                      [0, 1, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 1, 0],    # 14
                      [3, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 3]]    # 15


class Tile:

    def __init__(self, cords, bonus=0):
        self.cords = cords
        self.bonus = bonus
        self.str = BONUS_STRINGS[bonus]
        self.letter = ""
        self.in_use = False

    def to_string(self):
        return self.str

    def place_letter(self, letter):
        if self.in_use:
            return -1
        self.str = letter
        self.letter = letter
        self.in_use = True
        return self.bonus


class Board:

    def __init__(self):
        self.board = []
        for col in range(15):
            self.board.append([])
            for row in range(15):
                self.board.append([])
                self.board[row].append(Tile([row, col],
                                            BOARD_TILE_BONUSES[row][col]))

    def place_word(self, string, first_letter_cords, direction):
        is_valid = True
        end_cords = first_letter_cords.copy()
        for x in range(len(string)):
            end_cords = [end_cords[0] + directions[direction][0], end_cords[1] + directions[direction][1]]
            tile = self.board[end_cords[0]][end_cords[1]]
            if end_cords[1] < 0 or end_cords[1] == len(self.board[0]) or \
                    not tile.letter == "" or \
                    end_cords[0] < 0 or end_cords[0] == len(self.board):
                is_valid = False
                break
        if is_valid:
            end_cords = first_letter_cords.copy()
            for s in string:
                self.board[end_cords[0]][end_cords[1]].place_letter(s.lower())
                end_cords = [end_cords[0] + directions[direction][0], end_cords[1] + directions[direction][1]]
        return is_valid

    def to_string_bonuses(self):
        to_return = ""
        for col in self.board:
            for row in col:
                to_return += str(row.bonus) + ", "
            to_return += "\n"
        return to_return

    def to_string_strs(self):
        to_return = ""
        for col in self.board:
            for row in col:
                to_return += row.letter
            to_return += "\n"
        return to_return


# # # # # # # # # TESTING CODE START # # # # # # # # #
b = Board()
b.place_word("Sit", [0, 0], 3)
print(b.to_string_strs())
