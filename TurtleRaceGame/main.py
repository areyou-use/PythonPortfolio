"""
Simple race game with betting aaa
"""

from turtle import Turtle, Screen
from tkinter import messagebox
import random

play_game = True
screen = Screen()
screen.setup(width=500, height=400)
all_turtles = []
turtles_starting_y = -100
turtle_colors = ["red", "yellow", "green", "blue", "orange", "purple"]

def make_bet():
    while True:
        selected_color = screen.textinput(
            title="Make your bet", prompt="Select color \n(Red, Yellow, Green, Blue, Orange or Purple)"
        )
        if selected_color is None:
            messagebox.showinfo("Cancel", "Game finished.")
            screen.bye()
        selected_color = selected_color.strip().lower()
        if selected_color in turtle_colors:
            messagebox.showinfo("Bet!", f"You bet on the {selected_color} turtle.")
            return selected_color
        else:
            messagebox.showinfo("Warning", "Please select correct color.")

def setup_turtles():
    random.shuffle(turtle_colors)
    for color in turtle_colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=turtles_starting_y + (30 * turtle_colors.index(color)))
        all_turtles.append(new_turtle)

def race():
    race_on = True
    while race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    play_again = messagebox.askyesno(
                        title="Win", message=f"You've won. {winning_color} is the winner\n\n Play again?"
                    )
                    if not play_again:
                        messagebox.showinfo("Cancel", "Game finished.")
                        screen.bye()
                    else:
                        return play_again
                else:
                    play_again = messagebox.askyesno(
                        title="Lose", message=f"You've lost. {winning_color} is the winner\n\n Play again?"
                    )
                    if not play_again:
                        messagebox.showinfo("Cancel", "Game finished")
                        screen.bye()
                    else:
                        return play_again
            random_distance = random.randint(0, 20)
            turtle.forward(random_distance)
    return False

def setup_race():
    screen.clearscreen()
    all_turtles.clear()
    setup_turtles()

while play_game:
    setup_race()
    user_bet = make_bet()
    play_game = race()

screen.exitonclick()