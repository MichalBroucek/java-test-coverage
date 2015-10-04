#!/usr/bin/env python

import test_coverage_gui

__author__ = 'michal.broucek'


if __name__ == "__main__":
    """
    Create and start GUI for test coverage parser
    """
    gui = test_coverage_gui.Coverage_gui()
    gui.main_gui_loop()
