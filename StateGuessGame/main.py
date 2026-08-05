"""
US state guessing game with simple save system
"""

import turtle, pandas
from turtle import Turtle
from tkinter import messagebox

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()
answer_state = ""
keep_playing = True

screen.addshape(image)
turtle.shape(image)

def save_guessed_states():
    df = pandas.DataFrame(guessed_states)
    df.columns = ["state"]
    df.to_csv("guessed_states.csv", index=False)

def draw_state(state):
    found_state = data[data["state"] == state]
    """cache coordinates - need to get value as integer"""
    state_x = found_state["x"].iloc[0]
    state_y = found_state["y"].iloc[0]

    new_state_name = Turtle()
    new_state_name.penup()
    new_state_name.hideturtle()
    new_state_name.speed(0)

    new_state_name.goto(state_x, state_y)
    new_state_name.write(state, align="center", font=("Courier", 8, "normal"))

def restore_guessed_map():
    for single_state in guessed_states:
        draw_state(single_state)

def ask_for_state(answer):
    if answer is None:
        save_guessed_states()
        return False

    else:
        answer = answer.capitalize()
        print(answer)

        if answer == "Exit" or answer is None:
            save_guessed_states()
            return False

        elif answer in guessed_states:
            print("Already guessed")
            return True

        elif answer in all_states:
            draw_state(answer)
            guessed_states.append(answer)
            return True

        else:
            print("not found")
            return True

#-----------MAIN------------

continue_game = messagebox.askyesno(title="Continue", message="Continue game?")

if continue_game:
    guessed_states_data = pandas.read_csv("guessed_states.csv")
    guessed_states = guessed_states_data["state"].tolist()
    print(f"Guessed states: {guessed_states}")
    restore_guessed_map()
else:
    guessed_states = []

while len(guessed_states) < 50 and keep_playing == True:
    answer_state = screen.textinput(title=f"States guessed: {len(guessed_states)}", prompt="What's the name of another state?")
    keep_playing = ask_for_state(answer_state)
print("Game End")
