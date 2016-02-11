# This file has parts of my reading journal from day5 because
# of mac, jupyter, and TKinter issues.

# --- 4.1 --- #

from swampy.TurtleWorld import *
from math import cos, pi

world = TurtleWorld()
bob = Turtle()
print bob

bob.delay = 0

# for _ in range(4):
#     fd(bob, 100)
#     lt(bob)


# --- 4.2 --- #

# Oops, I already incorporated a loop in 4.1...

# --- 4.3 Exercises --- #

# 1.
def square(t):
    for _ in range(4):
        fd(t, 20)
        rt(t)

# square(bob)


# 2.
def square_with_length(t, length):
    for _ in range(4):
        fd(t, length)
        rt(t)

# square_with_length(bob, 50)


# 3.
def polygon(t, n, length):
    for _ in range(n):
        fd(t, length)
        lt(t, 360.0/n)

# polygon(bob, 5, 50)
# polygon(bob, 25, 10)


# 4.
def circle(t, r, n=100):
    length = 2*r*pi/n
    polygon(t, n, length)

# circle(bob, 100)


# 5.
def arc(t, r, angle, n=100):
    length = 2*r*pi/n
    for _ in range(n * angle/360):
        fd(t, length)
        rt(t, 360.0/n)

# arc(bob, 200, 90)


# --- 4.5 --- #
# Rewriting circle to infer a "good" n value:

def circle(t, r):
    n = int(2*r*pi)
    length = 2*r*pi/n
    polygon(t, n, length)

# circle(bob, 100)


def draw_flower(t, r):
    for _ in range(32):
        arc(t, r, 120)
        rt(t, 140)

draw_flower(bob, 100)



wait_for_user()
