import pgzrun
import random

WIDTH = 500
HEIGHT = 400

alien = Actor("alien")
alien.x = 250
alien.y = 200

sushi123456789101112131415161718192021222324252627282930 = "Click the alien to begin"

def draw():
    screen.fill("Indigo")
    alien.draw()
    screen.draw.text(sushi123456789101112131415161718192021222324252627282930,(150,50))

def on_mouse_down(pos):
    global sushi123456789101112131415161718192021222324252627282930
    if alien.collidepoint(pos):
        alien.x = random.randint(100,400)
        alien.y = random.randint(100,300)
        sushi123456789101112131415161718192021222324252627282930 = "Nice Shot!"
    else:
        sushi123456789101112131415161718192021222324252627282930 = "Unlucky..."

pgzrun.go()