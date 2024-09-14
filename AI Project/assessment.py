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
        dx, dy = direction
        new_x, new_y = grid.wrap_around(self.x + dx, self.y + dy)
        if grid.get_entity(new_x, new_y) is None:
            grid.remove_entity(self.x, self.y)  # Remove from old position
            self.x, self.y = new_x, new_y
            grid.place_entity(self, self.x, self.y)  # Place in new position
            self.energy -= 5

    def rest(self):
        self.energy += 10
        if self.energy > 100:
            self.energy = 100

    def action_to_direction(self, action):
        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        return directions.get(action, (0, 0))  # Default to no movement if invalid action


    def observe_state(self, grid):
        return (self.x, self.y)

    def calculate_reward(self, grid):
        # Reward: +10 for finding cheese, -10 for encountering a cat, otherwise 0
        entity = grid.get_entity(self.x, self.y)
        if isinstance(entity, Cheese):
            return 10
        elif isinstance(entity, Cat):
            return -10
        else:
            return 0


class QLearningMouse(Mouse):
    def __init__(self, gender):
        super().__init__(gender)
        self.q_table = {}  # Initialize Q-table
        self.alpha = 0.1  # Learning rate
        self.gamma = 0.9  # Discount factor
        self.epsilon = 0.1  # Exploration factor

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            # Explore: choose a random action
            return random.choice(['up', 'down', 'left', 'right', 'rest'])
        else:
            # Exploit: choose the best known action
            if state in self.q_table:
                return max(self.q_table[state], key=self.q_table[state].get)
            else:
                return random.choice(['up', 'down', 'left', 'right', 'rest'])

    def update_q_table(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = {a: 0 for a in ['up', 'down', 'left', 'right', 'rest']}
        best_future_q = max(self.q_table[next_state].values()) if next_state in self.q_table else 0
        self.q_table[state][action] += self.alpha * (reward + self.gamma * best_future_q - self.q_table[state][action])

    def act(self, grid):
        state = self.observe_state(grid)
        action = self.choose_action(state)

        # Perform the chosen action
        if action == 'rest':
            self.rest()
        else:
            dx, dy = self.action_to_direction(action)
            self.move((dx, dy), grid)

        # Update Q-table
        new_state = self.observe_state(grid)
        reward = self.calculate_reward(grid)
        self.update_q_table(state, action, reward, new_state)


class Cat:
    def __init__(self):
        self.energy = 100
        self.x = 0
        self.y = 0

    def move(self, grid, target_x, target_y):
        if self.energy <= 0:
            return
        dx = target_x - self.x
        dy = target_y - self.y
        if abs(dx) > abs(dy):
            dx = 1 if dx > 0 else -1
            dy = 0
        else:
            dy = 1 if dy > 0 else -1
            dx = 0
        new_x, new_y = grid.wrap_around(self.x + dx, self.y + dy)
        grid.remove_entity(self.x, self.y)
        self.x, self.y = new_x, new_y
        grid.place_entity(self, self.x, self.y)
        self.energy -= 5

    def calculate_distance(self, mouse):
        return abs(self.x - mouse.x) + abs(self.y - mouse.y)


class AICat(Cat):
    def __init__(self):
        super().__init__()
        self.decision_tree = self.build_decision_tree()

    def build_decision_tree(self):
        return {'energy': 50, 'distance': 3, 'action': ['play', 'attack']}

    def decide_action(self, mouse_distance):
        if self.energy < self.decision_tree['energy'] and mouse_distance <= self.decision_tree['distance']:
            return 'play'
        else:
            return 'attack'

    def act(self, mouse):
        mouse_distance = self.calculate_distance(mouse)
        action = self.decide_action(mouse_distance)
        if action == 'play':
            print(f"Cat is playing with mouse at ({mouse.x}, {mouse.y})")
            mouse.energy -= 5
        else:
            print(f"Cat is attacking mouse at ({mouse.x}, {mouse.y})")
            mouse.energy -= 20

