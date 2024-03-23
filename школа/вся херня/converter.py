from tkinter import *

class Convert:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("8400x7200")
        self.win.title("Конвертер градусов")
        
        self.label = Label(self.win, text="введите градусы", font=("Arial", 30, "bold"))
        self.label_fin = Label(self.win, text="", font=("Arial", 30, "bold"))
        self.entry = Entry(self.win, font=("Arial", 30, "bold"))
        self.btn = Button(self.win, text="конвертировать", command=self.run, font=("Arial", 30, "bold"))
        
    def run(self):
        self.label_fin.configure(text=f"{(int(self.entry.get()) * 9/5) + 32}")
        
        
    def main(self):
        self.label.pack()
        self.entry.pack()
        self.btn.pack()
        self.label_fin.pack()
        
        self.win.mainloop()
        
convert = Convert()
convert.main()