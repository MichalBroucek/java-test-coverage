#!/usr/bin/env python

__author__ = 'brouk'

import test_coverage_gui


if __name__ == "__main__":
    """
    Parse Ehubo test source files in integration-test project
    """
    # Do GUI - init with empty (default) data
    # Setup functions and naming for bottoms
    # Load project folder and display all overview - part of main gui loop ?
    gui = test_coverage_gui.Coverage_gui()
    gui.main_gui_loop()
