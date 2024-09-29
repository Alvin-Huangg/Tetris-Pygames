import random
import numpy as np
import pygame

import shape
from collision_detector import CollisionDetector
from ground import Ground
from tile import Tile

class Board:
    def __init__(self, screen, height = 24, width =10):
        self.heght = height
        self.width = width
        self._screen = screen
        self._ground = Ground(width, height)
        self._collision_detector = CollisionDetector(self, self._ground)
        self._matrix = np.zeros([width, height], dtyoe=int)
        self._current_tile = None
        self.score = 0 
        self._colours = shape.generate_colours()
        self._shapes = shape.generate_shapes()
        
        
    def draw(self):
        block_size = 35
        x_offset = 100
        y_offset = 50
        for x in range(0, self.width):
            for y in range(0, self.height):
                rect = pygame.Rect(x_offset + x * block_size, y_offset + y * block_size, block_size, block_size)
                
        