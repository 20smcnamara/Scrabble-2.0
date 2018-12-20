import pygame


def read_words():
    to_return = []
    file_object = open("words", "r")
    string = file_object.read()
    for word in string.split("\n"):
        to_return.append(word)
    return to_return


pygame.init()

display_width = 800
display_height = 800

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Scrabble')
Clock = pygame.time.Clock()
Clock.tick(60)
pygame.display.update()
game_exit = False

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
BONUS_STRINGS = ["", "2x\nWS", "2x\nLS", "3x\nWS", "3x\nLS", "Mid"]
#              Down    Right
directions = [[1, 0], [0, 1]]
words = read_words()
# The below board matches with a picture at
# https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwiukpWtt6ffAhXtlOAKHRfzAWkQjRx6BAgBEAU&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FScrabble&psig=AOvVaw20SSGA8_KK0jKP66a4O2It&ust=1545155611561682
#                      A  B  C  D  E  F  G  H  I  J  K  L  M  N  O
BOARD_TILE_BONUSES = [[3, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 3],    # 1
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
        if string in words:
            end_cords = first_letter_cords.copy()
            for x in range(len(string)):

                end_cords = [end_cords[0] + directions[direction][0], end_cords[1] + directions[direction][1]]
                if end_cords[1] < 0 or end_cords[1] == len(self.board) or \
                        end_cords[0] < 0 or end_cords[0] == len(self.board[0]):
                    print(end_cords)
                    is_valid = False
                    break
                tile = self.board[end_cords[0]][end_cords[1]]
                if not tile.letter == "":
                    is_valid = False
                    break
            if is_valid:
                end_cords = first_letter_cords.copy()
                for s in string:
                    self.board[end_cords[0]][end_cords[1]].place_letter(s.lower())
                    end_cords = [end_cords[0] + directions[direction][0], end_cords[1] + directions[direction][1]]
        else:
            is_valid = False
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


class ScrabbleGame:

    def __init__(self):
        self.board = Board()
        self.players = [Player(), Player(), Player(), Player()]
        self.x = 0

    def draw(self):
        # Some code
        self.x = 0

    def get_touch(self):
        # Some code
        self.x = 0

    def validate_touch(self):
        # Some code
        self.x = 0

# # # # # # # # # TESTING CODE START # # # # # # # # #
b = Board()
b.place_word("Sit", [14, 0], 0)
print(b.to_string_strs())
