import turtle, pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
guessed_states = []
data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()

screen.addshape(image)
turtle.shape(image)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"States guessed: {len(guessed_states)}", prompt="What's the name of another state?").capitalize()

    if answer_state == "Exit":
        df = pandas.DataFrame(guessed_states)
        df.to_csv("guessed_states.csv", index=False)
        break
    if answer_state in all_states:
        found_state = data[data["state"] == answer_state]
        """cache coordinates - need to get value as integer"""
        state_x = found_state["x"].iloc[0]
        state_y = found_state["y"].iloc[0]

        new_state_name = Turtle()
        new_state_name.penup()
        new_state_name.hideturtle()
        new_state_name.speed(0)

        new_state_name.goto(state_x, state_y)
        new_state_name.write(answer_state, align="center", font=("Courier", 8, "normal"))
        guessed_states.append(answer_state)
    else:
        print("not found")
