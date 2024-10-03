import math
from turtle import *

def heart(k):
    return 15 * math.sin(k) ** 3

def heart1(k):
    return 12 * math.cos(k) - 5 * \
        math.cos(2 * k) - 2 * \
        math.cos(3 * k) - \
        math.cos(4 * k)

speed(0)  # Vitesse maximale de dessin
bgcolor('black')
color('pink')
penup()  # Ne pas dessiner pendant qu'on se déplace au point de départ

# Se déplacer au premier point du cœur sans dessiner
goto(heart(0) * 20, heart1(0) * 20)
pendown()  # Commencer à dessiner le cœur

# Dessiner le cœur
for i in range(6000):
    x = heart(i) * 20
    y = heart1(i) * 20
    goto(x, y)

done()  # Terminer le dessin
