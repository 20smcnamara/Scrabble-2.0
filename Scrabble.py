import pygame
pygame.init()

display_width = 800
display_hight = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


class Tile:

    BONUS_CORDS = [[0, 0]]

    def __init__(self, cords, bonus):
        self.cords = cords
        self.letter = None


class Board:

    def __init(self):
        self.dick = "cheese"
        self.board = [[]]
