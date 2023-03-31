import turtle as t
import random
tim = t.Turtle()
t.colormode(255)

#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour=(r,g,b)
    colour=(r,g,b)
    return colour
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
       tim.forward(100)
       tim.right(angle)

for shape_side_n in range(3,15):
    tim.color(random_colour())
    draw_shape(shape_side_n)
