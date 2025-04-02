from tkinter import *
from tkinter.ttk import *
from time import strftime
import random

root = Tk()
root.title('Clock')

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
    fg_colors = [ '#0dd8de', '#22960d', '#0b0f7a', '#bed518', '#68332d', '#000000', '#342e7e']
    random_fg_color = random.choice(fg_colors)
    lbl.config(foreground=random_fg_color)
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='orange',)

lbl.pack(anchor='center')
time()
mainloop()
