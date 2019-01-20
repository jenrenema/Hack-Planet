# Planetary Model
import uagame
import pygame
import time
from pygame.locals import *


def main():

    # Create window
    width = 500
    height = 500
    window = uagame.Window('Move Test', width, height)
    window.set_auto_update(False)

    # Create game
    game = Game(window)

    # Play game
    game.play_game()

    # Close Window
    window.close()


class Game:
    # An object in this class represents a complete game

    def __init__(self, window):
        # Initialize a Game
        # - self is the Game to initialize
        # - window is a uagame.Window object

        self.window = window
        self.pause_time = 0.01
        self.close_clicked = False
        self.continue_game = True

    def play_game(self):
        # Play the game until the player presses the close button
        # - self is the Game
        while not self.close_clicked:
            self.handle_event()
            self.draw_frame()
            self.update_game_objects()
            time.sleep(self.pause_time)

    def handle_event(self):
        # Handle each user event
        # - self is the Game

        event = pygame.event.poll()
        if event.type == QUIT:
            self.close_clicked = True

    def update_game_objects(self):
        # Update the game objects
        # - self is the Game
        pass

    def draw_frame(self):
        # Draw all the game objects
        # - self is the Game
        self.window.clear()

        pygame.draw.rect(self.window.get_surface(), pygame.Color('Green'), pygame.Rect(100, 100, 100, 100))

        self.window.update()


class Block:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw_frame(self):

        pass

    def update_game_objects(self):
    	
    	pass




if __name__ == '__main__':
	main()