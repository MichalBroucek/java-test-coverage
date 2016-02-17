#!/usr/bin/env python

# todo:
# 1. make parsing folder persistent - DONE
# 2. add tab about test functionality coverage

import test_coverage_gui
import data_io

__author__ = 'michal.broucek'


if __name__ == "__main__":
    """
    Create and start GUI for test coverage parser
    """
    FOLDER_TO_PARSE = data_io.get_parsing_folder()
    gui = test_coverage_gui.Coverage_gui(FOLDER_TO_PARSE)
    gui.main_gui_loop()
