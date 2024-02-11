from datetime import datetime
from datetime import date
from tkinter import *

start_education_python = None


def calc(a):
    sec = a % 60
    a -= sec
    hour = int(a / 3600)
    min = int((a % 3600) / 60)
    print(f'{hour} hours {min} minutes {sec} seconds')
    return f'{hour}h {min}m {sec}s'


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.label_for_choise = Label(self, text="Choice leaning language")
        self.label_for_choise.grid(row=0, column=0, sticky=W)
        self.label_python = Label(self, text="python")
        self.label_python.grid(row=1, column=0, sticky=W)
        self.label_web = Label(self, text="WEB-Design")
        self.label_web.grid(row=1, column=1, sticky=W)
        self.button_python_start = Button(self, text="Start", command=self.start_for_education_python)
        self.button_python_start.grid(row=2, column=0, sticky=W)
        self.button_puthon_stop = Button(self, text="Stop", command=self.stop_education_python)
        self.button_puthon_stop.grid(row=3, column=0, sticky=W)
        self.button_web_start = Button(self, text="Start")
        self.button_web_start.grid(row=2, column=1, sticky=W)
        self.button_web_stop = Button(self, text="Stop")
        self.button_web_stop.grid(row=3, column=1, sticky=W)

    def start_for_education_python(self):
        global start_education_python
        start_education_python = datetime.now()
        print("START AT:", start_education_python)

    def stop_education_python(self):
        global now
        education_py = str(datetime.now() - start_education_python)[:7]
        a = (int(education_py[0]) * 3600) + (int(education_py[2:4]) * 60) + int(education_py[5:7])
        print("FINISH AT:", datetime.now())
        now = str(calc(a))
        f_1 = open("time_of_learning_python.txt", "r")
        data = f_1.read()
        f_1.close()
        int_time = int(data) + a
        all_time = calc(int(data) + a)

        self.label_python_now = Label(self, text="Nowadays")
        self.label_python_now.grid(row=4, column=0, sticky=W)
        self.output_ed_py_now = Text(self, width=10, height=1)
        self.output_ed_py_now.grid(row=5, column=0, sticky=W)
        self.output_ed_py_now.delete(0.0, END)
        self.output_ed_py_now.insert(0.0, now)
        self.label_python_all_times = Label(self, text="All times")
        self.label_python_all_times.grid(row=6, column=0, sticky=W)
        self.output_ed_py_all = Text(self, width=10, height=1)
        self.output_ed_py_all.grid(row=7, column=0, sticky=W)
        self.output_ed_py_all.delete(0.0, END)
        self.output_ed_py_all.insert(0.0, all_time)
        f_1 = open("time_of_learning_python.txt", "w")
        f_1.write(str(int_time))
        f_1.close()
        to_dict = dict(DATE = str(date.today()), TIME = str(now))
        print(to_dict)
        to_str =str(to_dict)
        with open("table_of_learning_python.txt", mode = "a") as table_python:
            table_python.write(f'\n{to_str}')
root = Tk()
root.title("Education")
root.geometry("300x200")
app = Application(root)
root.mainloop()
