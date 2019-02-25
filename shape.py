# Author: Rupa Karumanchi
# September 2018

#############################################################################

import turtle as t
import random
screen = t.Screen()

# Global constants for window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400


def init():
    """
    Initializing for drawing.
    Setting pen color to green and pensize to 2.
    Setting the speed of the turtle to 2.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :returns: None
    """
    t.color("midnight blue")
    t.pensize(2)
    t.speed(0)
    t.tracer(False)
    t.title('polygon')
    # Setting the initial position so that the drawing is better visible
    t.goto(-WINDOW_WIDTH / 4, -WINDOW_HEIGHT / 5)


#############################################################################


def polygon(sides, length, depth):
    """
    Drawing shape using turtle.
    :param sides: Length of sides
    :param length: Length
    :param depth: depth of diagram
    :returns: None
    """
    colors = ["medium violet red", "green", "midnight blue", "sky blue"]
    total = 0
    if sides > 2 and depth > 0:
        t.begin_fill()
        for index in range(sides):
            t.down()
            peri = length * sides
            total = total + peri
            t.forward(length + 10)

            t.up()
            t.forward(10)
            t.down()
            t.forward(8)
            t.left(360 / sides)
            polygon(sides - 1, length / 2.5, depth - 1)  # calling the function recursively

            for twinkle in range(6):
                t.left(60)
                t.forward(3)
                t.backward(3)
            t.up()

        t.end_fill()
        t.color(random.choice(colors)) # choosing a color at random
        t.fillcolor(random.choice(colors))
        print("Perimeter of shape is " + str(index) + " " + str(peri))
        print("Total length of all sides drawn so far is " + str(total))


def main():
    """
    The main function
    """
    init()
    polygon(5, 150, 3)
    t.mainloop()


if __name__ == '__main__':
    main()
