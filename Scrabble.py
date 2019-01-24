import pygame
import random
import time


def read_words():
    to_return = []
    file_object = open("words", "r")
    string = file_object.read()
    for word in string.split("\n"):
        to_return.append(word)
    return to_return


pygame.init()

display_width = 750
display_height = 800
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
light_blue = (33, 164, 215)
light_green = (120, 223, 17)
purple = (186, 85, 211)
blue = (0, 0, 205)
tan = (210, 180, 140)

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 75)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width/2), (display_height/2))
    game_display.blit(text_surf, text_rect)


TILE_AMOUNTS = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2,
                "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1}
BONUS_COLORS = [black, purple, light_blue, blue, red, black]
BONUS_STRINGS = ["", "2x\nWS", "2x\nLS", "3x\nWS", "3x\nLS", "Mid"]
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
#              Down    Right
directions = [[1, 0], [0, 1]]
words = read_words()
# The below board matches with a picture at https://en.wikipedia.org/wiki/Scrabble
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
        self.color = BONUS_COLORS[bonus]

    def to_string(self):
        return self.str

    def place_letter(self, letter):
        if self.in_use:
            return -1
        self.str = letter
        self.letter = letter
        self.in_use = True
        return self.bonus

    def is_empty(self):
        return self.letter == ""

    def draw(self):
        if self.bonus == 0:
            pygame.draw.rect(game_display, self.color, (self.cords[0], self.cords[1], length_board/15, height_board/15),
                             2)
        else:
            pygame.draw.rect(game_display, self.color, (self.cords[0], self.cords[1], length_board/15, height_board/15),
                             0)


class Board:

    def __init__(self):
        self.board = []
        for col in range(15):
            self.board.append([])
            for row in range(15):
                self.board.append([])
                self.board[row].append(Tile([row * (length_board / 15), col * (length_board / 15)],
                                            BOARD_TILE_BONUSES[row][col]))

    def place_word(self, string, first_letter_cords, direction):
        is_valid = True
        if string in words:
            end_cords = first_letter_cords.copy()
            for x in range(len(string)):

                end_cords = [end_cords[0] + directions[direction][0], end_cords[1] + directions[direction][1]]
                if end_cords[1] < 0 or end_cords[1] == len(self.board) or \
                        end_cords[0] < 0 or end_cords[0] == len(self.board[0]):
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

    def draw(self):
        for each in self.board:
            for x in each:
                x.draw()


class Player:

    def __init__(self, mode):
        self.letters = []
        self.x = 0

    def take_tiles(self, deck):
        while len(self.letters) < 7:
            if len(deck) > 0:
                self.letters.append(deck.pop(0))
            else:
                return True
        return False

    def prove_existence(self):
        self.x = 0
        print("I am a real thing")


class Human(Player):

    def __init__(self, mode=0):
        Player.__init__(self, mode)

    def check_touch(self):
        # Some code
        self.x = 0

    def draw_letters(self):
        # Some code
        self.x = 0

    def check_touch(self):
        # Some code
        self.x = 0


class Computer(Player):

    def __init__(self, mode=0):
        Player.__init__(self, mode)

    def take_turn(self):
        print("Beep Boop Code WIP")
        self.x = 0


class ScrabbleGame:

    def __init__(self):
        possible = [0, 0, 0, 1]
        self.board = Board()
        random_order = [possible.pop(random.randint(0, 3)),
                        possible.pop(random.randint(0, 2)),
                        possible.pop(random.randint(0, 1)),
                        possible.pop(0)]
        self.players = []
        for x in range(len(random_order)):
            if random_order[x] == 1:
                self.players.append(Human())
                self.player_index = x
            else:
                self.players.append(Computer())
        #        self.refill()
        self.deck = []
        # self.create_new_deck()
        # self.shuffle()
        self.refill()
        self.x = 0

    def create_new_deck(self):
        for letter in TILE_AMOUNTS.keys():
            for j in range(TILE_AMOUNTS[letter]):
                self.deck.append(letter)
        self.shuffle()

    def refill(self):
        for player in self.players:
            while player.take_tiles(self.deck):
                self.create_new_deck()

    def check_touch(self):
        self.players[self.player_index].check_touch()

    def validate_touch(self):
        # Some code
        self.x = 0

    def take_turns(self):
        self.players[self.player_index].get_move()
        for other in self.players:
            if not other == self.players[self.player_index]:
                other.take_turn()

    def shuffle(self):
        for x in range(len(self.deck)):
            switching_one = random.randint(0, len(self.deck) - 1)
            switching_two = random.randint(0, len(self.deck) - 1)
            while switching_two == switching_one:
                switching_one = random.randint(0, len(self.deck) - 1)
            temp = self.deck[switching_two]
            self.deck[switching_two] = self.deck[switching_one]
            self.deck[switching_one] = temp

    def draw(self):
        self.board.draw()


game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Scrabble')
Clock = pygame.time.Clock()
Clock.tick(60)
game_display.fill(white)
pygame.display.update()
game_exit = False
length_board = display_width  # Will be updated when more info provided
height_board = display_height  # Will be updated when more info provided
b = Board()
s = ScrabbleGame()
print(s.players[s.player_index].letters)
pygame.display.update()
while not game_exit:
    s.draw()
    for i in range(0, 750, 50):
        if i % 20 == 10:
            pygame.draw.rect(game_display, tan, (i, 750, 50, 50), 0)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if pygame.mouse.get_pressed() == (1, 0, 0):
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        while x % 50 != 0:
            x -= 1
        while y % 50 != 0:
            y -= 1
        pos_final = (x, y)
        print(pos_final)
