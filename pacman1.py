import pgzrun
import gameinput
import gamemaps
from random import randint
from datetime import datetime


WIDTH = 600
HEIGHT = 660


player = Actor("pacman_o") # Load in the player Actor image
SPEED = 3


def draw(): # Pygame Zero draw function
    global pacDots, player
    screen.blit('header', (0, 0))
    screen.blit('colourmap', (0, 80))
    pacDotsLeft = 0
    for a in range(len(pacDots)):
        if pacDots[a].status == 0:
            pacDots[a].draw()
            pacDotsLeft += 1
        if pacDots[a].collidepoint((player.x, player.y)):
            pacDots[a].status = 1
    if pacDotsLeft == 0: player.status = 2
    drawGhosts()
    getPlayerImage()
    player.draw()
    if player.status == 1:
        screen.draw.text(
            "GAME OVER",
             center=(300, 434),
             owidth=0.5,
             ocolor=(255, 255, 255),
             color=(255, 64, 0),
             fontsize=40)
    if player.status == 2:
        screen.draw.text(
            "YOU WIN!",
            center=(300, 434),
            owidth=0.5,
            ocolor=(255, 255, 255),
            color=(255, 64, 0),
            fontsize=40
        )




