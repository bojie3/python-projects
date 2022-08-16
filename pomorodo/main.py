from tkinter import *
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
reps = 1
time = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global time
    if time < 0:
        time = 0
        return
    minute = math.floor(count / 60)
    seconds = count % 60
    time = count
    if seconds < 10:
        seconds = '0' + str(seconds)
    canvas.itemconfig(timer_text, text=f'{minute}:{seconds}')
    if count > 0:
        windows.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

# create windows and screen
windows = Tk()
windows.title('pomodoro')
windows.config(padx=20, pady=20, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=2, column=2)

# create labels, buttons and functions
time_label = Label(text='Timer')
time_label.config(font=(FONT_NAME, 30, 'bold'), bg=YELLOW, fg=GREEN)
time_label.grid(row=1, column=2)
tick_label = Label(text='', bg=YELLOW, fg=GREEN)
tick_label.grid(row=3, column=2)


def start():
    global reps, time
    if reps > 8:
        reps = reps - 8
    if time > 0:
        time = 0
        return
    display = ''
    number = math.floor(reps / 2)  # usage of ceil will not work as it cannot separate properly
    for i in range(number):
        display += '✔'
    tick_label.config(text=display)
    if reps <= 6:
        if reps % 2 == 0:
            count_down(2)
            time_label.config(text='rest')
        else:
            count_down(5)
            time_label.config(text='work')
    else:
        if reps % 2 == 0:
            count_down(5)
            time_label.config(text='rest')
        else:
            count_down(5)
            time_label.config(text='work')
    reps += 1


def reset():
    """
    Another method is to use windows.after_cancel. Create a variable called timer, set it to none.
    In the count_down function, set timer to be equal to windows.after(1000, count_down, count - 1) in the if statement
    Then only need to change time to 0
    """
    global reps, time
    canvas.itemconfig(timer_text, text='00:00')
    reps = 1
    time = -1
    tick_label.config(text='', bg=YELLOW, fg=GREEN)
    time_label.config(text='timer')


start_button = Button(text='Start', command=start)
start_button.grid(row=3, column=1)
reset_button = Button(text='Reset', command=reset)
reset_button.grid(row=3, column=3)
windows.mainloop()
