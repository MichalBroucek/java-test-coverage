
import time
from Tkinter import *

import tkFileDialog
import constants
import data_io
from project_parser import Parser

__author__ = 'michal.broucek'

name = "Package "

class Coverage_gui():
    """
    Create GUI for java-test-coverage
    """

    def __init__(self, parsing_folder_name):

        self.folder_name = parsing_folder_name

        self.my_parser = None
        self.root = Tk()
        self.root.geometry("1000x900")
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
        self.simulator_test_button = Button(self.left_frame, text="Simulator tests", fg="black", state=DISABLED, width=20)
        self.simulator_test_button.pack(side=TOP)
        self.in_progress_test_button = Button(self.left_frame, text="In progress tests", fg="black", state=DISABLED, width=20)
        self.in_progress_test_button.pack(side=TOP)
        # New EHUBO feature groups
        self.otap_test_button = Button(self.left_frame, text="Otap tests", fg="black", state=DISABLED, width=20)
        self.otap_test_button.pack(side=TOP)
        self.gps_test_button = Button(self.left_frame, text="Gps tests", fg="black", state=DISABLED, width=20)
        self.gps_test_button.pack(side=TOP)
        self.modem_test_button = Button(self.left_frame, text="Modem tests", fg="black", state=DISABLED, width=20)
        self.modem_test_button.pack(side=TOP)
        self.bluetooth_test_button = Button(self.left_frame, text="Bluetooth tests", fg="black", state=DISABLED, width=20)
        self.bluetooth_test_button.pack(side=TOP)
        self.io_test_button = Button(self.left_frame, text="IO tests", fg="black", state=DISABLED, width=20)
        self.io_test_button.pack(side=TOP)
        self.can_test_button = Button(self.left_frame, text="CAN tests", fg="black", state=DISABLED, width=20)
        self.can_test_button.pack(side=TOP)
        self.distance_test_button = Button(self.left_frame, text="Distance tests", fg="black", state=DISABLED, width=20)
        self.distance_test_button.pack(side=TOP)
        self.mems_test_button = Button(self.left_frame, text="MEMs tests", fg="black", state=DISABLED, width=20)
        self.mems_test_button.pack(side=TOP)
        self.battery_test_button = Button(self.left_frame, text="Battery tests", fg="black", state=DISABLED, width=20)
        self.battery_test_button.pack(side=TOP)
        self.lifecycle_test_button = Button(self.left_frame, text="Lifecycle tests", fg="black", state=DISABLED, width=20)
        self.lifecycle_test_button.pack(side=TOP)
        self.storage_test_button = Button(self.left_frame, text="Storage tests", fg="black", state=DISABLED, width=20)
        self.storage_test_button.pack(side=TOP)
        self.degraded_test_button = Button(self.left_frame, text="Degraded tests", fg="black", state=DISABLED, width=20)
        self.degraded_test_button.pack(side=TOP)
        self.security_test_button = Button(self.left_frame, text="Security tests", fg="black", state=DISABLED, width=20)
        self.security_test_button.pack(side=TOP)
        self.tamper_test_button = Button(self.left_frame, text="Tamper tests", fg="black", state=DISABLED, width=20)
        self.tamper_test_button.pack(side=TOP)
        self.temperature_test_button = Button(self.left_frame, text="Temperature tests", fg="black", state=DISABLED, width=20)
        self.temperature_test_button.pack(side=TOP)
        self.assetracker_test_button = Button(self.left_frame, text="Assettracker tests", fg="black", state=DISABLED, width=20)
        self.assetracker_test_button.pack(side=TOP)
        self.installwizard_test_button = Button(self.left_frame, text="InstallWizard tests", fg="black", state=DISABLED, width=20)
        self.installwizard_test_button.pack(side=TOP)
        self.stability_test_button = Button(self.left_frame, text="Stability tests", fg="black", state=DISABLED, width=20)
        self.stability_test_button.pack(side=TOP)
        self.performance_test_button = Button(self.left_frame, text="Performance tests", fg="black", state=DISABLED, width=20)
        self.performance_test_button.pack(side=TOP)
        self.drivebuddy_test_button = Button(self.left_frame, text="DriveBuddy tests", fg="black", state=DISABLED, width=20)
        self.drivebuddy_test_button.pack(side=TOP)
        self.ruc_test_button = Button(self.left_frame, text="RUC tests", fg="black", state=DISABLED, width=20)
        self.ruc_test_button.pack(side=TOP)
        self.ui_test_button = Button(self.left_frame, text="UI tests", fg="black", state=DISABLED, width=20)
        self.ui_test_button.pack(side=TOP)
        self.endtoend_test_button = Button(self.left_frame, text="End-to-End tests", fg="black", state=DISABLED, width=20)
        self.endtoend_test_button.pack(side=TOP)
        self.other_test_button = Button(self.left_frame, text="Other tests", fg="black", state=DISABLED, width=20)
        self.other_test_button.pack(side=TOP)


        # Text area with scrollbar
        self.text_var = StringVar()
        self.text_var.set("Project data ...")
        self.scrollbar = Scrollbar(self.right_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text_widget = Text(self.right_frame, wrap=WORD, yscrollcommand=self.scrollbar.set)
        self.text_widget.insert(END, self.text_var.get())
        self.text_widget.pack(fill=BOTH, expand=YES)

        self.scrollbar.config(command=self.text_widget.yview)

    def __activate_all_buttons(self):
        """
        Activate all gui buttons if parsing folder is known
        :return:
        """
        if self.folder_name:
            for my_button in self.left_frame.children.values():
                my_button['state'] = NORMAL
            self.root.update()
        else:
            pass

    def __update_gui_after_parsing(self):
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
        self.simulator_test_button['command'] = self.simulator_tests
        self.in_progress_test_button['command'] = self.in_progress_tests
        # New EHUBO test groups
        self.otap_test_button['command'] = self.otap_tests
        self.gps_test_button['command'] = self.gps_tests
        self.modem_test_button['command'] = self.modem_tests
        self.bluetooth_test_button['command'] = self.bluetooth_tests
        self.io_test_button['command'] = self.io_tests
        self.can_test_button['command'] = self.can_tests
        self.distance_test_button['command'] = self.distance_tests
        self.mems_test_button['command'] = self.mems_tests
        self.battery_test_button['command'] = self.battery_tests
        self.lifecycle_test_button['command'] = self.lifecycle_tests
        self.storage_test_button['command'] = self.storage_tests
        self.degraded_test_button['command'] = self.degraded_tests
        self.security_test_button['command'] = self.security_tests
        self.tamper_test_button['command'] = self.tamper_tests
        self.temperature_test_button['command'] = self.temperature_tests
        self.assetracker_test_button['command'] = self.assettracker_tests
        self.installwizard_test_button['command'] = self.installwizard_tests
        self.stability_test_button['command'] = self.stability_tests
        self.performance_test_button['command'] = self.performance_tests
        self.drivebuddy_test_button['command'] = self.drivebuddy_tests
        self.ruc_test_button['command'] = self.ruc_tests
        self.ui_test_button['command'] = self.ui_tests
        self.endtoend_test_button['command'] = self.endtoend_tests
        self.other_test_button['command'] = self.other_tests


    def main_gui_loop(self):
        # Activate main gui loop
        self.my_parser = Parser(self.folder_name, constants.FILE_EXTENTION)
        self.__update_gui_after_parsing()
        self.__activate_all_buttons()
        self.root.mainloop()

    def askdirectory(self):
        """Load and parse project directory with updating gui"""
        dir_opt = {}
        folder = tkFileDialog.askdirectory(**dir_opt)
        print "Folder: " + folder
        self.my_parser = Parser(folder, constants.FILE_EXTENTION)
        self.__update_gui_after_parsing()
        # Save folder name for next call
        self.folder_name = folder
        data_io.save_parsing_folder(self.folder_name)
        self.__activate_all_buttons()
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

    def simulator_tests(self):
        """
        Display only simulator tests
        :return:
        """
        self.__update_tests_overview(constants.SIMULATOR_TESTS)
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

    def otap_tests(self):
        """
        Display otap tests only
        :return:
        """
        self.__update_tests_overview(constants.OTAP_TESTS)
        return

    def gps_tests(self):
        """
        Display GPS tests only
        :return:
        """
        self.__update_tests_overview(constants.GPS_TESTS)
        return

    def modem_tests(self):
        """
        Display modem tests only
        :return:
        """
        self.__update_tests_overview(constants.MODEM_TESTS)
        return

    def bluetooth_tests(self):
        """
        Display bluetooth tests only
        :return:
        """
        self.__update_tests_overview(constants.BLUETOOTH_TESTS)
        return

    def io_tests(self):
        """
        Display io tests only
        :return:
        """
        self.__update_tests_overview(constants.IO_TESTS)
        return

    def can_tests(self):
        """
        Display can tests only
        :return:
        """
        self.__update_tests_overview(constants.CAN_TESTS)
        return

    def distance_tests(self):
        """
        Display distance tests only
        :return:
        """
        self.__update_tests_overview(constants.DISTANCE_TESTS)
        return

    def mems_tests(self):
        """
        Display mems tests only
        :return:
        """
        self.__update_tests_overview(constants.MEMS_TESTS)
        return

    def battery_tests(self):
        """
        Display battery tests only
        :return:
        """
        self.__update_tests_overview(constants.BATTERY_TESTS)
        return

    def lifecycle_tests(self):
        """
        Display Lifecycle tests only
        :return:
        """
        self.__update_tests_overview(constants.LIFECYCLE_TESTS)
        return

    def storage_tests(self):
        """
        Display Storage/persistence tests only
        :return:
        """
        self.__update_tests_overview(constants.STORAGE_TESTS)
        return

    def degraded_tests(self):
        """
        Display degraded tests only
        :return:
        """
        self.__update_tests_overview(constants.DEGRADED_TESTS)
        return

    def security_tests(self):
        """
        Display security tests only
        :return:
        """
        self.__update_tests_overview(constants.SECURITY_TESTS)
        return

    def tamper_tests(self):
        """
        Display tamper tests only
        :return:
        """
        self.__update_tests_overview(constants.TAMPER_TESTS)
        return

    def temperature_tests(self):
        """
        Display temperature tests only
        :return:
        """
        self.__update_tests_overview(constants.TEMPERATURE_TESTS)
        return

    def assettracker_tests(self):
        """
        Display assettracker tests only
        :return:
        """
        self.__update_tests_overview(constants.ASSETTRACKER_TESTS)
        return

    def installwizard_tests(self):
        """
        Display InstallWizard tests only
        :return:
        """
        self.__update_tests_overview(constants.INSTALLWIZARD_TESTS)
        return

    def stability_tests(self):
        """
        Display stability tests only
        :return:
        """
        self.__update_tests_overview(constants.STABILITY_TESTS)
        return

    def performance_tests(self):
        """
        Display performance tests only
        :return:
        """
        self.__update_tests_overview(constants.PERFORMANCE_TESTS)
        return

    def drivebuddy_tests(self):
        """
        Display drivebuddy tests only
        :return:
        """
        self.__update_tests_overview(constants.DRIVEBUDDY_TESTS)
        return

    def ruc_tests(self):
        """
        Display RUC tests only
        :return:
        """
        self.__update_tests_overview(constants.RUC_TESTS)
        return

    def ui_tests(self):
        """
        Display UI tests only
        :return:
        """
        self.__update_tests_overview(constants.UI_TESTS)
        return

    def endtoend_tests(self):
        """
        Display end-to-end tests only
        :return:
        """
        self.__update_tests_overview(constants.ENDTOEND_TESTS)
        return

    def other_tests(self):
        """
        Display other tests only (non specific feature group)
        :return:
        """
        self.__update_tests_overview(constants.OTHER_TESTS)
        return


if __name__ == "__main__":
    my_gui = Coverage_gui()
    my_gui.main_gui_loop()
