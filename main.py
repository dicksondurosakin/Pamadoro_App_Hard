from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    canvas.itemconfig(text_canvas, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(fg=RED, bg=YELLOW, text="Break")
    elif reps % 2 == 1:
        count_down(WORK_MIN * 60)
        timer_label.config(fg=GREEN, bg=YELLOW, text="Work")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(fg=PINK, bg=YELLOW, text="Break")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    mins_left = math.floor(count/60)
    secs_left = count % 60
    if secs_left  < 10:
        secs_left = f"0{secs_left}"
    canvas.itemconfig(text_canvas, text=f"{mins_left}:{secs_left}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        checks = ""
        print(reps/2)
        for i in range(int(math.floor(reps/2))):
            checks += "✔️"
            check_mark_label.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=210, height=250, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(105, 105, image=tomato)
text_canvas = canvas.create_text(103, 135, text="00:00", fill="white", font= (FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=("arial", 30, "normal"))
timer_label.config(fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start",font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark_label = Label(text="", fg=GREEN, bg=YELLOW, font="bold")
check_mark_label.grid(row=2, column=1)
window.mainloop()