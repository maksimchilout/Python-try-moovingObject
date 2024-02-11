from tkinter import *
from tkinter import messagebox


def on_closing():
    if messagebox.askokcancel("Exit for application", "Do you want exit for application?"):
        tk.destroy()


tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Application")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=600, highlightthickness=0)
canvas.pack()

canvas1 = Canvas(tk, width=100, height=100)
canvas1.place(x=100, y=100, anchor=CENTER)
canvas1.create_rectangle(0,0, 100, 100, fill="red")

canvas2 = Canvas(tk, width=100, height=100)
canvas2.place(x=300, y=300, anchor=CENTER)
canvas2.create_oval(5,5, 95, 95, fill="red")
canvas2.create_oval(10,10, 90, 90, fill="yellow")


def drag(event):
   # print(event.x_root, event.y_root)

    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
   #print(mouse_x, mouse_y)
    event.widget.place(x=mouse_x, y=mouse_y, anchor=CENTER)


canvas1.bind("<B1-Motion>", drag)
canvas2.bind("<B1-Motion>", drag)

tk.mainloop()
