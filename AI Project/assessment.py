import random
import numpy as np
class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def wrap_around(self, x, y):
        return x % self.size, y % self.size

    def place_entity(self, entity, x, y):
        x, y = self.wrap_around(x, y)
        self.grid[x][y] = entity

    def remove_entity(self, x, y):
        x, y = self.wrap_around(x, y)
        self.grid[x][y] = None

    def get_entity(self, x, y):
        x, y = self.wrap_around(x, y)
        return self.grid[x][y]


class Cheese:
    def __init__(self, size, x, y):
        self.size = size
        self.nutritional_value = {'small': 5, 'medium': 10, 'large': 15}[size]
        self.x = x
        self.y = y

    def degrade(self):
        self.nutritional_value -= 0.1
        if self.nutritional_value < 0:
            self.nutritional_value = 0


class MouseHole:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cheese_storage = []
        self.occupants = []

    def store_cheese(self, cheese):
        self.cheese_storage.append(cheese)

    def add_mouse(self, mouse):
        if len(self.occupants) < 5:
            self.occupants.append(mouse)


class Mouse:
    def __init__(self, gender):
        self.gender = gender
        self.energy = 100
        self.x = 0
        self.y = 0
        self.carried_cheese = None

    def move(self, direction, grid):
        if self.energy <= 0:
            return
