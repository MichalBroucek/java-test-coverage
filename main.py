#!/usr/bin/env python

# todo:
# 1. make parsing folder persistent - DONE
# 2. add tab about test functionality coverage - DONE
# 3. generate .csv file for Jenkins plot plugin - DONE

import argparse
import os
import constants
import data_io
import test_coverage_gui
from project_parser import Parser

__author__ = 'michal.broucek'

def isFolderValid(folderPath):
    """
    Check if the 'folderPath' exists and it's valid folder
    """
    if os.path.isdir(folderPath):
        return True
    else:
        return False


if __name__ == "__main__":
    """
    Run program. Create and start GUI for test coverage parser or parse specific folder and generate *.csv file for Jenkins server
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", help="Parse specific folder which contents Gen2 tests. Generate *.csv file for Jenkins stats.")
    parser.add_argument("-v", "--verbose", help="Print test description: Feature, Scenario and Given strings in console output", action="store_true")
    args = parser.parse_args()

    if args.folder:
        # Parse specific folder and generate *.csv file for Jenkins server
        # Printout tests in specific groups into console output
        if os.path.isdir(args.folder):
            parser = Parser(args.folder, constants.FILE_EXTENTION)
            parser.do_parsing()                                                         # Parsing test groups
            print "\n\n"
            parser.print_jenkins_test_group_list(args.verbose)                          # Print out console output
            parser.generate_graph_data(parser, constants.JENKINS_PLOT_OUTPUT_FILE)      # Printout parsed data into file
        else:
            print "Folder '{0}' is invalid!".format(args.folder)
            print "Please specify correct folder."
    else:
        # Start main GUI app
        FOLDER_TO_PARSE = data_io.get_parsing_folder()
        gui = test_coverage_gui.Coverage_gui(FOLDER_TO_PARSE)
        gui.main_gui_loop()

    print "Exit."
