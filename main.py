#!/usr/bin/env python

# todo:
# 1. make parsing folder persistent
# 2. add tab about test functionality coverage

import test_coverage_gui

__author__ = 'michal.broucek'


def get_parsing_folder():
    """
    Try to load folder for parsing project
    """
    # 1. try to open text file
    # 2. try to load folder path
    # 3. return ehubo test path
    folder_path = ""
    return folder_path


if __name__ == "__main__":
    """
    Create and start GUI for test coverage parser
    """

    # todo: try to load persistent folder for passing
    # folder has to be saved when closing (or when was loaded for the first time)
    FOLDER_TO_PARSE = ""    # try to load load

    gui = test_coverage_gui.Coverage_gui()
    gui.main_gui_loop()
