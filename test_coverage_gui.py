__author__ = 'michal.broucek'

from Tkinter import *

test_groups = ["Smoke tests", "Regression tests", "Release tests", "Environment tests", "Emulator tests"]
name = "Package "


class Coverage_gui():
    """
    Create GUI for java-test-coverage
    """

    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x400")
        self.root.title("Gen2 test coverage")
        self.top_frame = LabelFrame(self.root, borderwidth=1)
        self.top_frame.pack(fill=X, side=TOP, padx=2, pady=2)
        self.bottom_frame = LabelFrame(self.root)
        self.bottom_frame.pack(fill=X, side=TOP, padx=2, pady=2)
        self.left_frame = Frame(self.bottom_frame)
        self.left_frame.pack(side=LEFT)
        self.right_frame = LabelFrame(self.bottom_frame, padx=2, pady=2)
        self.right_frame.pack(fill=X, side=TOP)
        # Default configuration of widget
        self.folder_button = Button(self.top_frame, text="Load project folder ...", fg="black", bd=3)
        self.folder_button.pack(side=RIGHT, padx=4, pady=4)
        self.folder_label = Label(self.top_frame, text="Loaded folder ...", fg="grey")
        self.folder_label.pack(side=RIGHT, padx=4, pady=4)

        for b_name in test_groups:
            self.b_name = Button(self.left_frame, text=b_name, fg="black")
            self.b_name.pack(side=TOP, fill=X)

        for number in range(10):
            button_name = "{0}{1}".format(name, number + 1)
            self.button_name = Button(self.left_frame, text=button_name, fg="black")
            self.button_name.pack(side=TOP, fill=X)

        default_text = "List of test\nwith basic description of tests.\nSeparate by test groups or specific package."
        self.text_content = Text(self.right_frame)
        self.text_content.insert(END, default_text)
        self.text_content.pack(side=RIGHT, padx=2, pady=2)

    def main_gui_loop(self):
        self.root.mainloop()


if __name__ == "__main__":
    my_gui = Coverage_gui()
    my_gui.main_gui_loop()
