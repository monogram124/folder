from tkinter import *
from PIL import Image, ImageTk
import random

class Game:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("700x600")
        self.win.resizable(0, 0)
        self.win.title("Rock Paper Scissors")
        self.win.config(bg="#FFFFFF")
        
        self.signs = ("rock", "paper", "scissors")

        self.rock_photo = ImageTk.PhotoImage(file="C:/Users/HYPERPC/Downloads/folder/школа/school_project/img/rock.png")
        self.paper_photo = ImageTk.PhotoImage(file="C:/Users/HYPERPC/Downloads/folder/школа/school_project/img/paper.png")
        self.scissors_photo = ImageTk.PhotoImage(file="C:/Users/HYPERPC/Downloads/folder/школа/school_project/img/scissors.png")
        
        self.gamepad_photo = Image.open("C:/Users/HYPERPC/Downloads/folder/школа/school_project/img/gamepad.jpg")
        self.resize_photo_gamepad = self.gamepad_photo.resize((150, 220))
        self.gamepad_photo = ImageTk.PhotoImage(self.resize_photo_gamepad)

        self.tick_photo = Image.open("C:/Users/HYPERPC/Downloads/folder/школа/school_project/img/tick.jpg")
        self.resize_photo_tick = self.tick_photo.resize((150, 220))
        self.tick_photo = ImageTk.PhotoImage(self.resize_photo_tick)

        self.cross_photo = Image.open("C:/Users/HYPERPC/Downloads/folder/школа/school_project/img/cross.jpg")
        self.resize_photo_cross = self.cross_photo.resize((150, 220))
        self.cross_photo = ImageTk.PhotoImage(self.resize_photo_cross)

        self.flag_photo = Image.open("C:/Users/HYPERPC/Downloads/folder/школа/school_project/img/flag.jpg")
        self.resize_photo_flag = self.flag_photo.resize((150, 220))
        self.flag_photo = ImageTk.PhotoImage(self.resize_photo_flag)

        self.rock_btn = Button(self.win, image=self.rock_photo, borderwidth=0, width=150, height=150, command=self.check_rock)
        self.paper_btn = Button(self.win, image=self.paper_photo, borderwidth=0, width=110, height=150, command=self.check_paper)
        self.scissors_btn = Button(self.win, image=self.scissors_photo, borderwidth=0, width=110, height=150, command=self.check_scissors)

        self.gamepad_lbl = Label(self.win, image=self.gamepad_photo, width=130, height=195)

        self.bot_photo = Image.open("C:/Users/HYPERPC/Downloads/folder/школа/school_project/img/robot.jpg")
        self.resize_photo_bot = self.bot_photo.resize((150, 220))
        self.bot_photo = ImageTk.PhotoImage(self.resize_photo_bot)

        self.bot_lbl = Label(self.win, image=self.bot_photo, width=110, height=170)
        
        self.bot_signs = {
            "rock": self.rock_photo,
            "paper": self.paper_photo,
            "scissors": self.scissors_photo
        }

    def check_rock(self):
        player_sign = "rock"
        bot_sign = random.choice(self.signs)

        if bot_sign == "paper":
            self.gamepad_lbl.config(image=self.cross_photo) # LOSE
            self.bot_lbl.config(image=self.bot_signs[bot_sign])
        elif bot_sign == "scissors":
            self.gamepad_lbl.config(image=self.tick_photo) # WIN
            self.bot_lbl.config(image=self.bot_signs[bot_sign])

        if player_sign == bot_sign:
            self.gamepad_lbl.config(image=self.flag_photo) # DRAW
            self.bot_lbl.config(image=self.bot_signs[bot_sign])

    def check_paper(self):
        player_sign = "paper"
        bot_sign = random.choice(self.signs)

        if bot_sign == "rock":
            self.gamepad_lbl.config(image=self.tick_photo) # WIN
            self.bot_lbl.config(image=self.bot_signs[bot_sign])

        elif bot_sign == "scissors":
            self.gamepad_lbl.config(image=self.cross_photo) # LOSE
            self.bot_lbl.config(image=self.bot_signs[bot_sign])

        if player_sign == bot_sign:
            self.gamepad_lbl.config(image=self.flag_photo) # DRAW
            self.bot_lbl.config(image=self.bot_signs[bot_sign])
    
    def check_scissors(self):
        player_sign = "scissors"
        bot_sign = random.choice(self.signs)

        if bot_sign == "rock":
            self.gamepad_lbl.config(image=self.cross_photo) # LOSE
            self.bot_lbl.config(image=self.bot_signs[bot_sign])

        elif bot_sign == "paper":
            self.gamepad_lbl.config(image=self.tick_photo) # WIN
            self.bot_lbl.config(image=self.bot_signs[bot_sign])

        if player_sign == bot_sign:
            self.gamepad_lbl.config(image=self.flag_photo) # DRAW
            self.bot_lbl.config(image=self.bot_signs[bot_sign])

    def run(self):
        
        self.gamepad_lbl.grid(column=1, pady=80)
        self.bot_lbl.grid(row=0, column=0)
        self.rock_btn.grid(row=1, column=0, padx=50)
        self.paper_btn.grid(row=1, column=1, padx=50)
        self.scissors_btn.grid(row=1, column=2, padx=50)
        
        
        self.win.mainloop()
        
game = Game()
game.run()