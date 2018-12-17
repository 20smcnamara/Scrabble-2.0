import pygame
pygame.init()

display_width = 800
display_hight = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


class Bonus:

    strs = ["", ]

    def __init__(self, bonus):
        self.bonus = bonus
        self.str = strs[bonus]


class Tile:

    BONUSES = []

    def __init__(self, cords, bonus=0):
        self.cords = cords
        self.bonus = bonus



class Board:

    def __init(self):
        self.dick = "cheese"
        self.board = [[]]
