from tkinter import *

import Maze_AStar as maze_a_star
import Maze_Tabu as maze_tabu


LIGHT_BG = "#ead8a0"
DARK_BG = "#d2ab4d"
BRONZE = '#CD7F32'
FONT = 'Times New Roman'
n = 0
speed = 0

def easy():
    n = 15
    speed = 100
    window.destroy()
    maze_a_star.main(n, speed)

def medium():
    n = 25
    speed = 3
    window.destroy()
    maze_a_star.main(n, speed)
    Tabu_view()


def hard():
    n = 75
    speed = 1
    window.destroy()
    maze_a_star.main(n, speed)

def difficulty():
    canvas.delete("all")
    ok_button.destroy()
    difficulty_label = Label(text="Select Difficulty", fg=DARK_BG, bg=LIGHT_BG, highlightthickness=0, font=(FONT, 30, "bold"))
    difficulty_label.place(x=150, y=50)

    easy_button = Button(text="   Easy   ", font=(FONT, 20, "bold"), fg=BRONZE, bg=LIGHT_BG, highlightthickness=0, command=easy)
    easy_button.place(x=225, y=150)

    medium_button=Button(text="Medium ", font=(FONT, 20, "bold"), fg=BRONZE, bg=LIGHT_BG, highlightthickness=0, command=medium)
    medium_button.place(x=225, y=250)

    hard_button = Button(text="   Hard   ", font=(FONT, 20, "bold"), fg=BRONZE, bg=LIGHT_BG, highlightthickness=0, command=hard)
    hard_button.place(x=225, y=350)

def Tabu_view():
    n = 25
    speed = 300
    maze_tabu.main2(n, speed)




window = Tk()
window.title("Maze-Solver")

canvas = Canvas(width=550, height=550, bg=LIGHT_BG)
bg_img = PhotoImage(file='BG_300_300.png')
# image = Image.open('BG_1.png')
# image = image.resize((100, 100), Image.ANTIALIAS)
canvas.create_image(275, 275, image=bg_img)
canvas.pack()

ok_button = Button(text="OK", font=(FONT, 20, "bold"), command=difficulty, bg=DARK_BG, fg=LIGHT_BG,highlightthickness=0)
ok_button.place(x=250, y=450)


window.mainloop()

