import pygame
import random
import time
from itertools import permutations


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
#global cords_letters
#cords_letters = {}


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text, a, b, size):
    large_text = pygame.font.Font('freesansbold.ttf', size)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = (a, b)
    game_display.blit(text_surf, text_rect)


def get_pos():
    while pygame.mouse.get_pressed() != (1, 0, 0):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            while x % 50 != 0:
                x -= 1
            while y % 50 != 0:
                y -= 1
            pos_final = (x, y)
            return pos_final


TILE_AMOUNTS = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2,
                "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1}
BONUS_COLORS = [black, purple, light_blue, blue, red, black]
BONUS_STRINGS = ["", "2x\nWS", "2x\nLS", "3x\nWS", "3x\nLS", "Mid"]
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
LETTER_VALUES = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3,
                 "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4,
                 "Z": 10}
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


def fastest_search(letters, starting_string=""):
    mixes = perm(letters, starting_string)
    print(mixes)
    good = []
    for x in mixes:
        if len(x) > 1:
            if x in words:
                good.append(x)
        # print(str(round(mixes.index(x) / len(mixes) * 100)) + "%")
    to_return = []
    for word in good:
        points = 0
        for letter in word:
            points += LETTER_VALUES[letter]
        to_return.append([word, points])
    for word in range(len(to_return)):
        for i in range(1, len(to_return)):
            if to_return[i][1] > to_return[i - 1][1]:
                temp = [to_return[i - 1][0], to_return[i - 1][1]]
                to_return[i - 1] = to_return[i]
                to_return[i] = temp
    return to_return


def perm(string, starting_string):
    to_return = []
    start = 2
    if len(starting_string) > 0:
        start = 1
    for x in range(start, len(string)):
        perms = (p for p in permutations(string, x))
        for p in perms:
            new_string_1 = starting_string + ''.join(p)
            new_string_2 = ''.join(p) + starting_string
            if new_string_1 not in to_return:
                to_return.append(new_string_1)
            if new_string_2 not in to_return:
                to_return.append(new_string_2)
    return to_return


class Deck:

    def __init__(self):
        self.letters = []

    def create_new_deck(self):
        for letter in TILE_AMOUNTS.keys():
            for j in range(TILE_AMOUNTS[letter]):
                self.letters.append(letter)
        self.shuffle()

    def shuffle(self):
        for x in range(len(self.letters)):
            switching_one = random.randint(0, len(self.letters) - 1)
            switching_two = random.randint(0, len(self.letters) - 1)
            while switching_two == switching_one:
                switching_one = random.randint(0, len(self.letters) - 1)
            temp = self.letters[switching_two]
            self.letters[switching_two] = self.letters[switching_one]
            self.letters[switching_one] = temp

    def reveal_letters(self):
        return self.letters

    def take_tile(self):
        return self.letters.pop()


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
            message_display(self.letter, self.cords[0], self.cords[1]+25, 40)
        else:
            pygame.draw.rect(game_display, self.color, (self.cords[0], self.cords[1], length_board/15, height_board/15),
                             0)
            message_display(self.letter, self.cords[0], self.cords[1]+25, 40)


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
            end_cords = [end_cords[1], end_cords[0]]
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
                end_cords = [end_cords[1], end_cords[0]]
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
            if len(deck.reveal_letters()) > 0:
                self.letters.append(deck.take_tile())
            else:
                return True
        return False

    def prove_existence(self):
        self.x = 0
        print("I am a real thing")

    def get_cords_letter(self):
        return self.cords_letters


class Human(Player):

    def __init__(self, mode=0):
        Player.__init__(self, mode)

    def draw_letters(self):
        for i in range(7):
            x = i*100
            message_display(self.letters[i], x+75, 775, 40)
#            cords_letters[(x+50, 750)] = self.letters[i]

    def skip_turn(self, deck, letters_being_swapped):
        for letter in letters_being_swapped:
            deck.append(letter)
        self.pick_new_letters()

    def pick_new_letters(self):
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
        self.deck = Deck()
        self.refill()
        self.x = 0

    def create_new_deck(self):
        self.deck.create_new_deck()

    def refill(self):
        for player in self.players:
            while player.take_tiles(self.deck):
                self.create_new_deck()

    def validate_touch(self):
        # Some code
        self.x = 0

    def take_turns(self):
        player_move = self.players[self.player_index].get_move()
        if len(player_move) > 0:
            self.players[self.player_index].skip_turn(self.deck.reveal_letters(), player_move)
            self.shuffle()
            self.refill()
        for other in self.players:
            if not other == self.players[self.player_index]:
                other.take_turn()

    def shuffle(self):
        self.deck.shuffle()

    def draw(self):
        game_display.fill(white)
        for i in range(0, 750, 50):
            if i % 20 == 10:
                pygame.draw.rect(game_display, tan, (i, 750, 50, 50), 0)
        self.board.draw()
        self.players[self.player_index].draw_letters()


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
scrabbleGame = ScrabbleGame()
print(scrabbleGame.players[scrabbleGame.player_index].letters)
pygame.display.update()
scrabbleGame.draw()


def game_loop():
    while not game_exit:
        pygame.display.update()
        skip = 0
        message_display("do you want to skip, y or n?", 375, 325, 40)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    skip = True
                if event.key == pygame.K_n:
                    skip = False
            game_display.fill(white)
            scrabbleGame.draw()

        if skip is False:
            message_display("what word do you want to spell?", 375, 325, 40)
            pygame.display.update()
            w = input("word? ")
            scrabbleGame.draw()
            message_display("X coordinate?", 375, 325, 40)
            pygame.display.update()
            x = int(input("x? "))
            scrabbleGame.draw()
            message_display("y coordinate?", 375, 325, 40)
            pygame.display.update()
            y = int(input("y? "))
            scrabbleGame.draw()
            message_display("Direction down(0) or right(1)?", 375, 325, 40)
            pygame.display.update()
            d = int(input("direction? "))
            scrabbleGame.draw()
            b.place_word(w, ((x - 1), (y - 1)), d)

        if skip is True:
            Human.skip_turn()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


game_loop()