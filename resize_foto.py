from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image


class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.but_open_file = Button(self, text="Choice folder", command=self.open_file)
        self.but_open_file.grid(row=0, column=0, sticky=W)
        self.but_save_file = Button(self, text="Choice folder", command=self.save_file)
        self.but_save_file.grid(row=1, column=0, sticky=W)
        self.guess_x = Entry(self)
        self.guess_x.grid(row=2, column=0, sticky=W)
        self.guess_Y = Entry(self)
        self.guess_Y.grid(row=3, column=0, sticky=W)
        self.but_processing = Button(self, text="Apply", command=self.apply)
        self.but_processing.grid(row=4, column=0, sticky=W)

    directory_open = None
    directory_to_save = None

    def apply(self):
        try:
            resize_x_to_min = int(self.guess_x.get())
            resize_y_to_min = int(self.guess_Y.get())
            with os.scandir(path=directory_open) as it:
                for entry in it:
                    if not entry.is_file():
                        print("dir:\t" + entry.name)
                    else:
                        if str(entry.name).endswith(".JPG"):
                            print("file:\t" + entry.name)
                            size = (resize_x_to_min, resize_y_to_min)
                            img_obj = Image.open(directory_open + "/" + entry.name)
                            img_obj.thumbnail(size)
                            img_obj.show()
                            img_obj.save(directory_to_save + "/" + entry.name)
        except:
            print("Error of processing")
            pass

    def open_file(self):
        file_name = fd.askdirectory()
        global directory_open
        directory_open = file_name

    def save_file(self):
        file_name = fd.askdirectory()
        global directory_to_save
        directory_to_save = file_name


root = Tk()
root.title("Size variation of foto")
root.geometry("300x200")
app = Application(root)
root.mainloop()
