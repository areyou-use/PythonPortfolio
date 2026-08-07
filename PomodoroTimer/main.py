"""
Pomodoro timer app
"""

from tkinter import *
import math

BREAK_LABEL_COLOR = "#ff8000"
WORK_LABEL_COLOR = "#1fb55d"
BG_COLOR = "#ebf2fc"
FONT_NAME = "Arial"

WORK_MIN = 25 #25
SHORT_BREAK_MIN = 5 #5
LONG_BREAK_MIN = 20 #20
REPS = 0
timer = None
timer_on = False

def start_timer():
    global timer_on
    if not timer_on:
        timer_on = True
        global REPS
        REPS += 1
        if REPS == 8:
            count_down(LONG_BREAK_MIN * 60)
            timer_label.config(text="BREAK", fg=BREAK_LABEL_COLOR)
        elif REPS % 2 != 0:
            count_down(WORK_MIN * 60)
            timer_label.config(text="FOCUS", fg=WORK_LABEL_COLOR)
        elif REPS % 2 == 0:
            count_down(SHORT_BREAK_MIN * 60)
            timer_label.config(text="BREAK", fg=BREAK_LABEL_COLOR)
            checkmarks_label.config(text="")
        if REPS == 9:
            REPS = 0
            marks = ""
            checkmarks_label.config(text=marks)

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global timer_on
        timer_on = False
        start_timer()
        marks =""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks_label.config(text=marks)

def reset_timer():
    window.after_cancel(timer)
    checkmarks_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="POMODORO", fg=WORK_LABEL_COLOR)
    global REPS
    REPS = 0
    global timer_on
    timer_on = False

#-----------------MAIN----------------------

window = Tk()
CANVAS_HEIGHT = 300
CANVAS_WIDTH = 300
window.config(padx=30, pady=30, bg=BG_COLOR)
window.title("POMODORO TIMER")

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BG_COLOR, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
tomato_img = tomato_img.subsample(3)
canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=tomato_img)
timer_text = canvas.create_text(145, 160, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="POMODORO", fg=WORK_LABEL_COLOR, bg=BG_COLOR, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

checkmarks_label = Label(fg=WORK_LABEL_COLOR, bg=BG_COLOR, anchor="n", font=(FONT_NAME,12))
checkmarks_label.grid(column=1, row=3)

button_start = Button(text="Start", width=7, height=1, command=start_timer, font=(FONT_NAME, 16))
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", width=7, height=1, command=reset_timer, font=(FONT_NAME, 16))
button_reset.grid(column=2, row=2)


window.mainloop()