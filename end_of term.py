from tkinter import *
from datetime import date


def countin(guess):
    temp = guess.split(".")
    dt = date(int(temp[0]), int(temp[1]), int(temp[2]))
    rem = dt - date.today()
    day = int(rem.days)

    return day



class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.inst_lb = Label(self, text="Enter end of your term:")
        self.inst_lb.grid(row=0, column=0, columnspan=2, sticky=W)
        self.ent = Entry(self)
        self.ent.grid(row=1, column=0, columnspan=2, sticky=W)
        self.but = Button(self, text="CoUnT", command=self.count)
        self.but.grid(row=1, column=2, sticky=W)

    def count(self):
        guess = self.ent.get()
        self.day = Label(self, text="Days")
        self.day.grid(row=2,column=1, sticky=W)
        self.output = Text(self, width=10, height=1)
        self.output.grid(row=2, column=0, sticky=W)
        self.output.delete(0.0, END)
        self.output.insert(0.0, countin(guess))
        self.output_hours = Text(self, width=10, height=1)
        self.output_hours.grid(row=3, column=0, sticky=W)
        self.output_hours.delete(0.0, END)
        self.output_hours.insert(0.0, countin(guess)*24)
        self.hours = Label(self, text="Hours")
        self.hours.grid(row=3,column=1, sticky=W)
        self.output_minutes = Text(self, width=10, height=1)
        self.output_minutes.grid(row=4, column=0, sticky=W)
        self.output_minutes.delete(0.0, END)
        self.output_minutes.insert(0.0, countin(guess)*1440)
        self.minutes = Label(self, text="Minutes")
        self.minutes.grid(row=4,column=1, sticky=W)
        self.output_secundes = Text(self, width=10, height=1)
        self.output_secundes.grid(row=5, column=0, sticky=W)
        self.output_secundes.delete(0.0, END)
        self.output_secundes.insert(0.0, countin(guess)*86400)
        self.seconds = Label(self, text="Seconds")
        self.seconds.grid(row=5,column=1, sticky=W)


root = Tk()
root.title("End")
root.geometry("300x200")
app = Application(root)
root.mainloop()
