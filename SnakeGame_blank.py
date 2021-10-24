import pygame
import sys
import time
import random

from pygame.locals import *

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
GRIDSIZE = 20
GRID_WIDTH = WINDOW_WIDTH / GRIDSIZE
GRID_HEIGHT = WINDOW_HEIGHT / GRIDSIZE

WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
ORANGE = (255, 165, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

FPS = 10

class Python(object):
  """
  이 곳에 코드를 작성해주세요.
  """


class Feed(object):
  """
  이 곳에 코드를 작성해주세요.
  """
  
  

def draw_object(surface, color, pos):
  """
  이 곳에 코드를 작성해주세요.
  """

def check_eat(python, feed):
  """
  이 곳에 코드를 작성해주세요.
  """
  
def show_info(length, speed, surface):
  font = pygame.font.Font(None, 34)
  text = font.render("Length: " + str(length) + "  Speed: " + str(round(speed, 2)), 1, GRAY)
  pos = text.get_rect()
  pos.centerx = 150
  surface.blit(text, pos)


if __name__ == '__main__':
  python = Python()
  feed = Feed()

  pygame.init()
  window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
  pygame.display.set_caption('Python Game')
  surface = pygame.Surface(window.get_size())
  surface = surface.convert()
  surface.fill(WHITE)
  clock = pygame.time.Clock()
  pygame.key.set_repeat(1, 40)
  window.blit(surface, (0, 0))

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == KEYDOWN:
        if event.key == K_UP:
          python.control(UP)
        elif event.key == K_DOWN:
          python.control(DOWN)
        elif event.key == K_LEFT:
          python.control(LEFT)
        elif event.key == K_RIGHT:
          python.control(RIGHT)

    surface.fill(WHITE)
    python.move()
    check_eat(python, feed)
    speed = (FPS + python.length) / 2
    show_info(python.length, speed, surface)
    python.draw(surface)
    feed.draw(surface)
    window.blit(surface, (0,0))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(speed)
