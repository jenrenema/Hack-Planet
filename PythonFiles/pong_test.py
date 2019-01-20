# Pong Game
import uagame
import pygame
import time
from pygame.locals import *


def main():

   # Create window
   width = 800
   height = 500
   window = uagame.Window('Pong', width, height)
   window.set_auto_update(False)
   window.set_font_size(100)

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

       self.object_color = pygame.Color('white')
       self.ball = Ball(self.window, self.object_color)
       self.paddle_width = 14
       self.paddle_height = 60
       self.paddles = [pygame.Rect(100, (int(self.window.get_height()) - self.paddle_height) / 2, self.paddle_width,
                                   self.paddle_height),
                       pygame.Rect(int(self.window.get_width()) - 100 - self.paddle_width,
                                   (int(self.window.get_height()) - self.paddle_height) / 2, self.paddle_width,
                                   self.paddle_height)]

       self.scores = [Score('left', self.window), Score('right', self.window)]

       self.key_pressed = [False, False, False, False]  # represents the 'q', 'a', 'p', and 'l' keys respectively

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

       correct_keys = [K_q, K_a, K_p, K_l]
       list_of_keys = pygame.key.get_pressed()
       for index in range(len(correct_keys)):
           if list_of_keys[correct_keys[index]]:
               self.key_pressed[index] = True
           else:
               self.key_pressed[index] = False

   def update_game_objects(self):
       # Update the game objects
       # - self is the Game

       self.move_paddle()
       self.ball.hit_edge(self.scores)
       self.ball.hit_paddle(self.paddles)
       self.ball.move()

   def draw_frame(self):
       # Draw all the game objects
       # - self is the Game

       self.window.clear()
       self.ball.draw()
       for index in range(2):
           pygame.draw.rect(self.window.get_surface(), self.object_color, self.paddles[index])
           Score.draw(self.scores[index])
       self.window.update()

   def should_continue(self):
       # Check if the game should continue
       # - self is the Game

       for score in self.scores:
           if score.get_value() == 11:
               self.continue_game = False

   def move_paddle(self):
       # Move the paddles
       # - self is the Game

       if self.key_pressed[0] and self.paddles[0].top > 0:
           self.paddles[0].move_ip(0, -2)
       if self.key_pressed[1] and self.paddles[0].bottom < self.window.get_height():
           self.paddles[0].move_ip(0, 2)
       if self.key_pressed[2] and self.paddles[1].top > 0:
           self.paddles[1].move_ip(0, -2)
       if self.key_pressed[3] and self.paddles[1].bottom < self.window.get_height():
           self.paddles[1].move_ip(0, 2)


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

   def hit_edge(self, scores):
       # Checks if the ball is at the edge of the window and updates the velocity and score accordingly
       # - self is the Ball
       # - scores is an array of Score objects

       if self.center[0] + self.velocity[0] > self.window.get_width():
           self.velocity[0] = -self.velocity[0]
           scores[0].increment()
       elif self.center[0] + self.velocity[0] < 0:
           self.velocity[0] = -self.velocity[0]
           scores[1].increment()
       elif self.center[1] + self.velocity[1] > self.window.get_height() or self.center[1] + self.velocity[1] < 0:
           self.velocity[1] = -self.velocity[1]

   def hit_paddle(self, paddles):
       # Checks if the Ball collides with a paddle and update velocity accordingly
       # - self is the Ball
       # - paddles is an array of Rect objects that represent the paddles

       if paddles[0].collidepoint(self.center[0] + self.velocity[0], self.center[1]):
           self.velocity[0] = abs(self.velocity[0])
       elif paddles[1].collidepoint(self.center[0] + self.velocity[0], self.center[1]):
           self.velocity[0] = -abs(self.velocity[0])


class Score:
   # An object in this class represents a players score

   def __init__(self, side, window):
       # Initialize a Score
       # - self is the Score to initialize
       # - side is a string representing the side of the screen the score should be displayed
       # - window is a uagame.Window object

       self.window = window
       self.value = 0
       self.side = side
       if self.side == 'left':
           self.coords = [5, 0]
       else:
           self.coords = [self.window.get_width() - self.window.get_string_width(str(self.value)), 0]

   def increment(self):
       # Add one to the score
       # - self is the Score

       self.value += 1
       if self.side == 'right':
           self.coords[0] = self.window.get_width() - self.window.get_string_width(str(self.value))

   def draw(self):
       # Draw the score
       # - self is the Score

       self.window.draw_string(str(self.value), self.coords[0], self.coords[1])

   def get_value(self):
       # Returns the current value of the Score
       # - self is the Score
       # return: An integer value of the Score

       return self.value


main()
    
