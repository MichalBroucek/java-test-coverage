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

    # path = "/home/brouk/workspacePython/testCoverage/project-data-src/"
    # path = "/home/brouk/workspacePython/testCoverage/integration-test/automation-portal/src/test/java/nz/co/eroad/automation/tests/ehubo/"
    #path = r"""C:\workspace\integration-test\automation-portal\src\test\java\nz\co\eroad\automation\tests\ehubo"""

    gui = test_coverage_gui.Coverage_gui()

    gui.main_gui_loop()

    # TODO: parse in gui like that
    # my_parser = Parser(path, constants.FILE_EXTENTION)
    # my_parser.do_parsing()

    # for test_description in my_parser.test_descriptions:
    #     print "\n---------------------------------------------------------"
    #     print test_description.to_string()
    #     print "---------------------------------------------------------\n"

    # my_parser.create_overview_file("test_overview_output.txt")
    # my_parser.create_complete_file("test_complete_output.txt")

    # for test_group in constants.TEST_GROUPS:
    #     file_name = "test_group_{0}_output.txt".format(test_group)
    #     print "Debug: " + file_name
    #     #my_parser.create_test_group_file(test_group, file_name)

    print "Done."

