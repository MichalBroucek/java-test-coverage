__author__ = 'michal.broucek'

from Tkinter import *

root = Tk()
load_folder_frame = Frame(root)
load_folder_frame.pack(side=TOP)

data_frame = Frame(root)
data_frame.pack(side=BOTTOM)

folder_label = Label(load_folder_frame, text="Actual loaded folder ...")
folder_label.pack(side=LEFT)

folder_buttom = Button(load_folder_frame, text="Load project folder", fg="black")
folder_buttom.pack(side=LEFT)

data_frame = Frame(root)
data_frame.pack(side=BOTTOM)

data_label_1 = Label(data_frame, text="Data label 1 ...")
folder_label.pack(side=BOTTOM)
data_label_2 = Label(data_frame, text="Data label 2 ...")
data_label_2.pack(side=TOP)
data_label_3 = Label(data_frame, text="Data label 3 ...")
data_label_3.pack(side=TOP)
data_label_4 = Label(data_frame, text="Data label 4 ...")
data_label_4.pack(side=TOP)

root.mainloop()
