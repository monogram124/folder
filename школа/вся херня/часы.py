from tkinter import *
from PIL import ImageTk, Image

class Window:
    def __init__(self):
        self.win = Tk()
        self.photo = Image.open("C:/Users/HYPERPC/Downloads/folder/школа/clock.png")
        self.resize_photo = self.photo.resize((50, 50))
        self.photo = ImageTk.PhotoImage(self.resize_photo)

        self.photo2 = Image.open("C:/Users/HYPERPC/Downloads/folder/школа/shamil.png")
        self.resize_photo2 = self.photo2.resize((300, 920))
        self.photo2 = ImageTk.PhotoImage(self.resize_photo2)
        
        self.win.iconphoto(False, self.photo)
        self.win.geometry("300x300")
        
        self.btn = Button(self.win, image=self.photo)
        self.btn2 = Button(self.win, image=self.photo2)
        
    def main(self):
        self.btn.pack()
        self.btn2.pack()
        self.win.mainloop()
        
win = Window()
win.main()