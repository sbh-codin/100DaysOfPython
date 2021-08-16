import turtle #as turtle_module

# himmy = turtle_module.Turtle()
himmy = turtle.Turtle()
himmy.shape("triangle")
#Challenge1
# for i in range(4):
#     himmy.forward(100)
#     himmy.left(90)

# print(himmy)
#
# import turtle
# from turtle import TurtleScreen
# timmy = turtle.Turtle()
# timmy.shape("triangle")

# timmy.forward(50)
# timmy.left(90)
# timmy.forward(50)
# timmy.left(90)
# timmy.forward(50)
# timmy.left(90)
# timmy.forward(50)
# print(timmy)

#Challenge 2
# for i in range(50):
#     himmy.penup()
#     himmy.forward(10)
#     himmy.pendown()
#     himmy.forward(10)

#Challenge 3
# for side in range(3,9):
#     angle = 360//side
#     for _ in range(side):
#         himmy.forward(50)
#         himmy.left(angle)

#Challenge 4
# # himmy.speed("fastest")
# for tilt in range(0,360,10):
#     himmy.setheading(tilt)
#     # for _ in range(360):
#     himmy.circle(100)
#         # himmy.forward(1)
#         # himmy.left(1)


#Main Challenge
# import colorgram

# colors = colorgram.extract('images.jpg', 30)

# extracted_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_rgb =(r, g, b)
#     extracted_colors.append(color_rgb)
# print(extracted_colors)

import random

colors = [(220, 154, 97), (122, 170, 201), (42, 110, 156), (235, 203, 98), (206, 137, 161), (155, 63, 90), (123, 187, 159), (199, 82, 108), (30, 135, 100), (220, 85, 64), (165, 164, 46), (236, 162, 181), (159, 76, 53), (53, 169, 133), (241, 167, 156), (33, 164, 194), (154, 212, 194), (8,
102, 74), (140, 33, 45), (109, 116, 170), (147, 209, 222), (179, 183, 217), (130, 38, 32), (39, 58, 108), (23, 56, 84), (68, 38, 33)]

turtle.colormode(255)
himmy.penup()
himmy.speed("fastest")
himmy.setheading(220)
himmy.forward(300)
himmy.setheading(0)
for dot in range(1, 101):
    himmy.dot(20, random.choice(colors))
    himmy.forward(50)
    if dot%10 == 0:
        himmy.setheading(90)
        himmy.forward(50)
        himmy.setheading(180)
        himmy.forward(500)
        himmy.setheading(0)

stay = turtle.Screen()
stay.exitonclick()