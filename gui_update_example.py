__author__ = 'brouk'

import tkFileDialog
import constants

from Tkinter import *
from time import sleep

# root = Tk()
# var = StringVar()
# var.set('hello')
#
# l = Label(root, textvariable = var)
# l.pack()
#
# for i in range(6):
#     sleep(1) # Need this to slow the changes down
#     var.set('goodbye' if i%2 else 'hello')
#     root.update_idletasks()


root = Tk()
root.geometry("750x500")
root.title("GUI update example")
top_frame = LabelFrame(root, borderwidth=1)
top_frame.pack(fill=X, side=TOP, padx=2, pady=2)

my_text = StringVar()
my_text.set('Text text text')

lab = Label(top_frame, textvariable=my_text).pack(side=LEFT)
my_text.set("Text text text")
root.update()

#root.mainloop()
#root.update_idletasks()

sleep(3)
my_text.set('.... .... ....')
#root.update_idletasks()
root.update()
sleep(3)
my_text.set('Text text text')
#root.update_idletasks()
root.update()
sleep(3)
my_text.set('.... .... ....')
#root.update_idletasks()
root.update()

exit()
