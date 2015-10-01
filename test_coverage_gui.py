
__author__ = 'michal.broucek'

import tkFileDialog
import constants

from Tkinter import *
from project_parser import Parser

test_groups = ["Smoke tests", "Regression tests", "Release tests", "Environment tests", "Emulator tests"]
name = "Package "

dir_opt = {}
my_parser = None

class Coverage_gui():
    """
    Create GUI for java-test-coverage
    """

    def __init__(self):
        self.root = Tk()
        self.root.geometry("750x500")
        self.root.title("Gen2 test coverage")
        self.top_frame = LabelFrame(self.root, borderwidth=1)
        self.top_frame.pack(fill=X, side=TOP, padx=2, pady=2)
        self.bottom_frame = LabelFrame(self.root)
        self.bottom_frame.pack(fill=X, side=TOP, padx=2, pady=2)
        self.left_frame = Frame(self.bottom_frame)
        self.left_frame.pack(side=LEFT)
        self.right_frame = LabelFrame(self.bottom_frame, padx=2, pady=2)
        self.right_frame.pack(fill=X, side=RIGHT)
        # Default configuration of widget
        self.folder_button = Button(self.top_frame, text="Load project folder ...", fg="black", bd=3,
                                    command=self.askdirectory)
        self.folder_button.pack(side=RIGHT, padx=4, pady=4)
        self.folder_label = Label(self.top_frame, text="Loaded folder ...", fg="grey")
        self.folder_label.pack(side=RIGHT, padx=4, pady=4)

        self.detail_check_box = Checkbutton(self.left_frame, text="Show details", fg="black")
        self.detail_check_box.pack(side=TOP, fill=X)

        self.all_tests_button = Button(self.left_frame, text="All tests", fg="black")
        self.all_tests_button.pack(side=TOP, fill=X)

        for b_name in test_groups:
            self.b_name = Button(self.left_frame, text=b_name, fg="black")
            self.b_name.pack(side=TOP, fill=X)

        for number in range(10):
            button_name = "{0}{1}".format(name, number + 1)
            self.button_name = Button(self.left_frame, text=button_name, fg="black")
            self.button_name.pack(side=TOP, fill=X)

        self.text_var = StringVar()
        self.text_var.set("... test data ...")
        self.text_content = Label(self.right_frame, textvariable=self.text_var)
        self.text_content.pack(side=RIGHT, padx=2, pady=2)

    def main_gui_loop(self):
        self.root.mainloop()

    def askdirectory(self):
        """Returns a selected directoryname."""
        folder = tkFileDialog.askdirectory(**dir_opt)
        print "Folder: " + folder
        global my_parser
        my_parser = Parser(folder, constants.FILE_EXTENTION)
        my_parser.do_parsing()
        formated_content = my_parser.get_output("ALL")
        # for test_description in my_parser.test_descriptions:
        #     print "\n---------------------------------------------------------"
        #     print test_description.to_string()
        #     print "---------------------------------------------------------\n"
        self.text_var.set(formated_content)
        self.root.update()
        return


if __name__ == "__main__":
    my_gui = Coverage_gui()
    my_gui.main_gui_loop()

    # Get all buttons as descendant (content) of left frame ...
    # for ...
