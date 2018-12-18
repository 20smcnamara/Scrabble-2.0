import pygame
pygame.init()

display_width = 800
display_hight = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
BONUS_STRINGS = ["", "2x\nWS", "2x\nLS", "3x\nWS", "3x\nLS"]
            #   Up     Down      Left    Right
directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

# The below board matches with a picture at
# https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwiukpWtt6ffAhXtlOAKHRfzAWkQjRx6BAgBEAU&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FScrabble&psig=AOvVaw20SSGA8_KK0jKP66a4O2It&ust=1545155611561682
BOARD_TILE_BONUSES = [[3, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 3],
                      [0, 1, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 1, 0],
                      [0, 0, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 1, 0, 0],
                      [2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0],
                      [3, 0, 0, 1, 0, 0, 0, 5, 0, 0, 0, 1, 0, 0, 3],
                      [0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 4, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                      [2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 2],
                      [0, 0, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 1, 0, 0],
                      [0, 1, 0, 0, 0, 4, 0, 0, 0, 4, 0, 0, 0, 1, 0],
                      [3, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 3]]


class Tile:

    def __init__(self, cords, bonus=0):
        self.cords = cords
        self.bonus = bonus
        self.str = BONUS_STRINGS[bonus]

    def to_string(self):
        return self.str

    def place_letter(self, letter):
        self.str = letter
        return self.bonus


class Board:

    def __init__(self):
        self.board = []
        for col in range(10):
            self.board.append([])
            for row in range(10):
                self.board.append([])
                self.board[row][col] = Tile([row, col], BOARD_TILE_BONUSES[row][col])

    def place_word(self, string, first_letter_cords, direction):
        is_valid = True
        end_cords = first_letter_cords
        for x in range(len(string)):
            end_cords += directions[direction]
            if end_cords[1] < 0 or end_cords[1] == len(self.board[0]) or \
                    not self.board[end_cords[0]][end_cords[1]].to_string() == "" or \
                    end_cords[0] < 0 or end_cords[0] == len(self.board):
                is_valid = False
                break
        if is_valid:
            end_cords = first_letter_cords
            for s in string:
                self.board[end_cords[0]][end_cords[1]]
                first_letter_cords += directions[direction]

        return is_valid



# # # # # # # # # TESTING CODE START # # # # # # # # #
b = Board()
b.place_word("Sit", [0, 0], 3)
