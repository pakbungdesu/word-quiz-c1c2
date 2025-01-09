
from tkinter import *

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.canvas = None
        self.txt = None
        self.blank = None
        self.img = None
        self.one = None
        self.two = None
        self.three = None
        self.four = None

    def set_window(self, title, pdx, pdy, theme):
        self.window.title(title)
        self.window.config(padx=pdx, pady=pdy, background=theme)

    def set_canvas(self, wd, ht, bg, highlight=0):
        self.canvas = Canvas(width=wd, height=ht, background=bg, highlightthickness=highlight)
        self.canvas.grid(row=1, column=0, columnspan=2)

    def set_blank(self, txt, fg, bg, fnt):
        self.blank = Label(text=txt, fg=fg, bg=bg, font=(fnt, 10))
        self.blank.grid(row=2, column=0)


    def write_canvas(self, x, y, w, txt, color, fnt):
        self.canvas.delete("all")  # Clears everything on the canvas
        self.txt = self.canvas.create_text(x, y, text=txt, width=w, fill=color, font=fnt)

    def set_button(self, t1, t2, t3, t4, color, commands, highlight=0):
        self.img = PhotoImage(file="myrect.png")

        self.one = Button(
            image=self.img,
            text=t1,
            compound="center",  # Places text on top of the image
            highlightthickness=highlight,
            command=commands[0],  # Assign the first command
            bg=color,
            activebackground=color,
            borderwidth=0
        )
        self.one.grid(row=3, column=0, columnspan=2)

        self.two = Button(
            image=self.img,
            text=t2,
            compound="center",
            highlightthickness=highlight,
            command=commands[1],  # Assign the second command
            bg=color,
            activebackground=color,
            borderwidth=0
        )
        self.two.grid(row=4, column=0, columnspan=2)

        self.three = Button(
            image=self.img,
            text=t3,
            compound="center",
            highlightthickness=highlight,
            command=commands[2],  # Assign the third command
            bg=color,
            activebackground=color,
            borderwidth=0
        )
        self.three.grid(row=5, column=0, columnspan=2)

        self.four = Button(
            image=self.img,
            text=t4,
            compound="center",
            highlightthickness=highlight,
            command=commands[3],  # Assign the fourth command
            bg=color,
            activebackground=color,
            borderwidth=0
        )
        self.four.grid(row=6, column=0, columnspan=2)

    def run(self):
        self.window.mainloop()
