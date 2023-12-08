import pygame
import sys
from components import Card, BlackJack

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 1400, 800
FPS = 30

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Your existing code for creating cards
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

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("darkgreen")
    # Draw the cards (you need to implement the drawing logic)
    # ...

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
