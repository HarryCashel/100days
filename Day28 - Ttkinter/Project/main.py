import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="  Timer  ")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Quick Break.", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work Time!", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    check = "✓"
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    formatted = f"{minutes}:{seconds}"

    canvas.itemconfig(timer_text, text=formatted)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        window.bell()
        start_timer()
        completed_work_session = math.floor(reps / 2)
        if reps % 2 == 0:
            check_mark.config(text=f"{check * completed_work_session} ")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Image canvas widget properties
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Timer label widget and properties
timer_label = tk.Label(text="  Timer  ", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

# Check label Widget
check_mark = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=3)

# Start Button

start = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

# Reset Button

reset = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
