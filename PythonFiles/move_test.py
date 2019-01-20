# Pong Game
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
       self.pause_time = 0.005
       self.close_clicked = False
       self.continue_game = True

       self.key_pressed = [False, False, False, False]

   def play_game(self):
       # Play the game until the player presses the close button
       # - self is the Game

       while not self.close_clicked:

           self.handle_event()
           self.draw_frame()
           if self.continue_game:
               self.update_game_objects()
               self.should_continue()
           time.sleep(self.pause_time)

   def handle_event(self):
       # Handle each user event
       # - self is the Game

       event = pygame.event.poll()
       if event.type == QUIT:
           self.close_clicked = True

       correct_keys = [K_a, K_s, K_w, K_d]
       list_of_keys = pygame.key.get_pressed()
       for index in range(len(correct_keys)):
           if list_of_keys[correct_keys[index]]:
               self.key_pressed[index] = True
           else:
               self.key_pressed[index] = False

   def update_game_objects(self):
       # Update the game objects
       # - self is the Game


   def draw_frame(self):
       # Draw all the game objects
       # - self is the Game

       self.window.clear()

       pygame.draw.circle(self.window.get_surface(), pygame.Color("White"), [int(self.window.get_width()/2), int(self.window.get_height()/2)], 2)

       self.window.update()

   def should_continue(self):
       # Check if the game should continue
       # - self is the Game
       self.continue_game = True


class Ball:
   # An object in this class represents a circle

   def __init__(self, window, color):
       # Initialize a Ball
       # - self is the Ball to initialize
       # - window is a uagame.Window object
       # - color is a pygame.Color object representing the color of the ball

       self.radius = 7
       self.color = color
       self.center = [int(window.get_width()/2), int(window.get_height()/2)]
       self.velocity = [5, 1]
       self.window = window

   def draw(self):
       # Draw the Ball
       # - self is the Ball

       pygame.draw.circle(self.window.get_surface(), self.color, self.center, self.radius)

   def move(self):
       # Move the Ball
       # - self is the Ball

       for index in range(2):
           self.center[index] += self.velocity[index]

main()
    
