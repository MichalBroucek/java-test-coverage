
import time
from Tkinter import *

import tkFileDialog
import constants
from project_parser import Parser

__author__ = 'michal.broucek'

test_groups = ["Smoke tests", "Regression tests", "Release tests", "Environment tests", "Emulator tests"]
name = "Package "

class Coverage_gui():
    """
    Create GUI for java-test-coverage
    """

    def __init__(self):
        self.my_parser = None
        self.root = Tk()
        self.root.geometry("1000x600")
        self.root.title("Gen2 test coverage")
        self.top_frame = LabelFrame(self.root, borderwidth=1)
        self.top_frame.pack(fill=X, side=TOP, padx=2, pady=2)
        self.bottom_frame = LabelFrame(self.root)
        self.bottom_frame.pack(fill=BOTH, expand=YES, side=TOP, padx=2, pady=2)
        self.left_frame = Frame(self.bottom_frame)
        self.left_frame.pack(fill=Y, side=LEFT)
        self.right_frame = LabelFrame(self.bottom_frame, padx=2, pady=2)
        self.right_frame.pack(fill=BOTH, expand=YES, side=TOP)
        # Default configuration of widget
        self.folder_button = Button(self.top_frame, text="Load project folder ...", fg="black", bd=3,
                                    command=self.askdirectory)
        self.folder_button.pack(side=RIGHT, padx=4, pady=4)
        self.label_text = StringVar()
        self.label_text.set('Project folder ...')
        self.folder_label = Label(self.top_frame, textvariable=self.label_text, fg="grey")
        self.folder_label.pack(side=RIGHT, padx=4, pady=4)
        # All buttons non active till project folder is loaded
        #self.detail_check_box = Checkbutton(self.left_frame, text="Show details", fg="black", state=DISABLED)
        #self.detail_check_box.pack(side=TOP)
        self.all_tests_button = Button(self.left_frame, text="All tests", fg="black", state=DISABLED, width=20)
        self.all_tests_button.pack(side=TOP)
        self.smoke_test_button = Button(self.left_frame, text="Smoke tests", fg="black", state=DISABLED, width=20)
        self.smoke_test_button.pack(side=TOP)
        self.regression_test_button = Button(self.left_frame, text="Regression tests", fg="black", state=DISABLED, width=20)
        self.regression_test_button.pack(side=TOP)
        self.release_test_button = Button(self.left_frame, text="Release tests", fg="black", state=DISABLED, width=20)
        self.release_test_button.pack(side=TOP)
        self.environment_test_button = Button(self.left_frame, text="Environment tests", fg="black", state=DISABLED, width=20)
        self.environment_test_button.pack(side=TOP)
        self.emulator_test_button = Button(self.left_frame, text="Emulator tests", fg="black", state=DISABLED, width=20)
        self.emulator_test_button.pack(side=TOP)
        self.in_progress_test_button = Button(self.left_frame, text="In progress tests", fg="black", state=DISABLED, width=20)
        self.in_progress_test_button.pack(side=TOP)
        # Text area with scrollbar
        self.text_var = StringVar()
        self.text_var.set("Project data ...")
        self.scrollbar = Scrollbar(self.right_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text_widget = Text(self.right_frame, wrap=WORD, yscrollcommand=self.scrollbar.set)
        self.text_widget.insert(END, self.text_var.get())
        self.text_widget.pack(fill=BOTH, expand=YES)

        self.scrollbar.config(command=self.text_widget.yview)

    def main_gui_loop(self):
        self.root.mainloop()

    def askdirectory(self):
        """Load and parse project directory with updating gui"""
        dir_opt = {}
        folder = tkFileDialog.askdirectory(**dir_opt)
        print "Folder: " + folder
        self.my_parser = Parser(folder, constants.FILE_EXTENTION)
        # Update label
        self.label_text.set(self.my_parser.project_path)
        self.root.update()
        self.my_parser.do_parsing()
        # update text field
        self.text_widget.delete('1.0', END)
        formatted_content = self.my_parser.get_output(constants.ALL_TESTS)
        self.text_var.set(formatted_content)
        self.text_widget.insert(END, self.text_var.get())
        # Setup functions to all buttons
        self.all_tests_button['command'] = self.all_tests
        self.smoke_test_button['command'] = self.smoke_tests
        self.regression_test_button['command'] = self.regression_tests
        self.release_test_button['command'] = self.release_tests
        self.regression_test_button['command'] = self.regression_tests
        self.emulator_test_button['command'] = self.emulator_tests
        self.environment_test_button['command'] = self.environment_tests
        self.in_progress_test_button['command'] = self.in_progress_tests

        # Activate all buttons
        for my_button in self.left_frame.children.values():
            my_button['state'] = NORMAL
        self.root.update()
        return

    def __update_tests_overview(self, test_group):
            """
            Display specific group of tests
            :return:
            """
            self.text_widget.delete('1.0', END)
            self.text_var.set("")
            self.text_widget.insert(END, self.text_var.get())
            self.root.update()
            time.sleep(0.2)
            self.text_widget.delete('1.0', END)
            formatted_content = self.my_parser.get_output(test_group)
            self.text_var.set(formatted_content)
            self.text_widget.insert(END, self.text_var.get())
            self.root.update()
            return

    def all_tests(self):
        """
        Display all projects tests
        :return:
        """
        self.__update_tests_overview(constants.ALL_TESTS)
        return

    def smoke_tests(self):
        """
        Display only smoke tests
        :return:
        """
        self.__update_tests_overview(constants.SMOKE_TESTS)
        return

    def regression_tests(self):
        """
        Display only regression tests
        :return:
        """
        self.__update_tests_overview(constants.REGRESSION_TESTS)
        return

    def release_tests(self):
        """
        Display only release tests
        :return:
        """
        self.__update_tests_overview(constants.RELEASE_TESTS)
        return

    def environment_tests(self):
        """
        Display only environment tests
        :return:
        """
        self.__update_tests_overview(constants.ENVIRONMENTAL_TESTS)
        return

    def emulator_tests(self):
        """
        Display emulator tests only
        :return:
        """
        self.__update_tests_overview(constants.EMULATOR_TESTS)
        return

    def in_progress_tests(self):
        """
        Display emulator tests only
        :return:
        """
        self.__update_tests_overview(constants.IN_PROGRESS_TESTS)
        return

if __name__ == "__main__":
    my_gui = Coverage_gui()
    my_gui.main_gui_loop()
