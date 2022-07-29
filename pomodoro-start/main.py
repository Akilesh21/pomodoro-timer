from cgitb import text
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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text ="00:00")
    timer_text1.config(text="Timer")
    check_text.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_Sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps ==8:    
        count_down(long_break_sec)
        timer_text1.config(text="LONG BREAK",fg="#e2979c")
    elif reps % 2 ==0:    
        count_down(short_break_sec)
        timer_text1.config(text="SHORT BREAK",fg="#f7f5dd")
    else:    
        count_down(work_Sec)
        timer_text1.config(text="WORK",fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min =math.floor(count/60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"     
    canvas.itemconfig(timer_text,text =f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count -1)
    else:
        start_timer()
        marks = ""
        work_session =math.floor(reps/2)
        for i in range(work_session):
            marks +="✓"
        check_text.config(text = marks)    
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg="#9bdeac")
#timer_text
timer_text1 = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg="#e7305b",bg="#9bdeac",highlightthickness=0)
timer_text1.grid(column=2,row=0)
#check_text
check_text = Label(font=(FONT_NAME,15,"bold"),fg="#e7305b",bg="#9bdeac",highlightthickness=0)
check_text.grid(column=2,row=3)
canvas = Canvas(width=200,height=224,bg="#9bdeac",highlightthickness=0)
tomato_img = PhotoImage(file="tkinter_gui/pomodoro-start/tomato.png")
canvas.create_image(100,112,image = tomato_img)
canvas.grid(column=2,row=1)
#for timer count_down
timer_text = canvas.create_text(100,130,text ="00.00",fill="white",font=(FONT_NAME,35,"bold"))

#start button
start_button = Button(text="Start",command=start_timer)
start_button.grid(column=0,row=3)
#reset_button
reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=3,row=3)
window.mainloop()
