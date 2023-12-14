import pygame
import sys
from components import Card, BlackJack

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 1400, 800
FPS = 30

suits = ['hearts', 'diamonds', 'spades', 'clubs']
courts = ['king', 'queen', 'jester']
placeholder = 'Enter index # or letter'
cards = list()
for value in range(1, 14):
    for suit in suits:
        if value == 1:
            cards.append(Card('Ace', value, suit))
        elif value > 10:
            cards.append(Card(courts[11 - value], 10, suit))
        else:
            cards.append(Card(value, value, suit))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack Game")

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill("darkgreen")

    
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
