__author__ = 'brouk'

import constants
import sys


def get_parsing_folder():
    """
    Try to load folder for parsing project
    """
    folder_path = ""
    try:
        with open(constants.PARSING_FOLDER_FILE_NAME_STORAGE, 'r') as folder_file:
            folder_path = folder_file.readline()
            print "Parsing folder: ", folder_path
    except IOError as ioErr:
        print "IOError: ", ioErr
        #pass
    except:
        print "Unexpected Error: ", sys.exc_info()[0]
        raise

    return folder_path


def save_parsing_folder(folder_path):
    """
    Save new parsing folder absolute path into the text file
    :return:
    """
    path_saved = False
    with open(constants.PARSING_FOLDER_FILE_NAME_STORAGE, 'w') as folder_file:
        folder_file.write(folder_path)
        path_saved = True
    return path_saved
