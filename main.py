from turtle import Turtle, Screen
import random

screen = Screen()                 # Create screen object
screen.setup(width = 500, height = 400)       # set specific width and height of the turtle window
user_choice = screen.textinput(title = "Make your bet", prompt = "Which turtle will win? Enter a color: ").lower()    # pop up dialogue window for user input


colors = ["red", "orange", "yellow", "green", "blue", "purple"]   # create list of colors

all_turtles = []      # Create empty list so i can append object instances t to it for each iteration
                      # this list will be iterated to check distance travelled by that individual object turtle to see who wins

y_starting_position = -150
for index in range(6):     # iterate 6 times (since 6 colors) through 0 to 5
    t = Turtle(shape="turtle")  # Create objects of turtles' names, and change its shape to a turtle
    t.color(colors[index])
    t.penup()                   # so that line won't be drawn when turtle moves to left corner
    y_starting_position += 50        # add 50 to y-coordinates for every iteration
    t.goto(x = -250, y = y_starting_position)     # shift turtle to starting position coordinates --> x coordinates same for all, only y diff
    all_turtles.append(t)            # append all the object instances t to the empty list for each iteration

is_still_racing = True      # Create flag variable for while loop
while is_still_racing:      # while True

    for each_turtle in all_turtles:         # iterate through each turtle to see who reached finishing point first

        if each_turtle.xcor() > 230:             # when 1 turtle reach end of map (aka right side of window)
            is_still_racing = False      # Stop while loop, ends race once there's a winner
            winner_color = each_turtle.pencolor()     # find the color of the winning turtle

            if winner_color == user_choice:
                print(f"Congrats, you won! The winning turtle's color is {winner_color}.")
            else:                           # if user guessed wrongly
                print(f"Aww, you lost! The winning turtle's color is {winner_color}.")

        random_distance = random.randint(0,10)          # distance travelled by each turtle will be randomly chosen
        each_turtle.forward(random_distance)


screen.exitonclick()                            # window only close when i click outside of it



