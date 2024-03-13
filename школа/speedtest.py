from tkinter import *
from PIL import ImageTk, Image

class ClickerGame:
    def __init__(self):
        self.win = Tk()
        self.win.title("Кликер")
        self.win.geometry("1002x476")
        
        self.counter = 0
        
        self.btn = Button(self.win, text="Нажми меня", command=self.click, font=("Arial", 30, "bold"))
        self.label = Label(self.win, text="0", font=("Arial", 30, "bold"))
        
        self.win_bg = PhotoImage(file="tkinter/speedtest/shamil.png", width=1002, height=476)
        self.bg_logo = Label(self.win, image=self.win_bg)
        
    def click(self):
        self.counter += 1
        self.label.config(text=f"{self.counter}")
        
    def main(self):
        self.btn.place(x=501, y=100)
        self.label.place(x=501, y=200)
        self.bg_logo.place(x=0, y=0)
        
        self.win.mainloop()
    
clicker = ClickerGame()        
clicker.main()