#!/usr/bin/env python
__author__ = 'brouk'

import constants
import os
import sys

from test_description import TestDescription

class Parser:
    """
    Parser class to initialize parsing environment, perform parsing and provide results
    """

    def __init__(self, project_path, file_extension):
        """
        Init environment
        :return:
        """
        self.project_path = project_path
        self.file_extension = file_extension
        self.test_descriptions = []
        self.__line = '--------------------------------------------------------------------------------------------------------------'

    def parsing_java_file(self, absoluth_path, directory, file_name):
        """
        Parsing one file to search SCENARION, FEATURE, WHEN, THEN, ...
        :param absoluth_path: filename of text file to parse
        :return: list of String OR list of class ?
        """

        file_description = TestDescription()
        file_description.folder_name = directory
        file_description.file_name = file_name

        try:
            file = open(absoluth_path, 'r')
            for line in file:
                line = line.strip()

                # Ignore empty lines and lines with white space characters only
                if line:
                    if line.isspace():
                        continue
                else:
                    continue

                if line.startswith(constants.PACKAGE):
                    file_description.package = line.split(constants.PACKAGE, 1)[1]
                    continue
                elif line.startswith(constants.TEST_GROUP_LABEL):
                    file_description.test_groups = self.__get_test_groups(line)
                    continue
                elif line.startswith(constants.FEATURE):
                    line = line.split(constants.FEATURE, 1)[1]
                    file_description.feature = self.__decorate_desription_line(line, constants.FEATURE)
                    continue
                elif line.startswith(constants.SCENARIO):
                    line = line.split(constants.SCENARIO, 1)[1]
                    file_description.scenario = self.__decorate_desription_line(line, constants.SCENARIO)
                    continue
                elif line.startswith(constants.GIVEN):
                    line = line.split(constants.GIVEN, 1)[1]
                    file_description.given = self.__decorate_desription_line(line, constants.GIVEN)
                    continue

                for item in constants.DESCRIPTION_ITEMS_LIST:
                    if line.startswith(item):
                        line = line.split(item, 1)[1]
                        line = self.__decorate_desription_line(line, item)
                        file_description.actionList.append(line)

        except IOError as e:
            print "I/O Error(({0}): {1}) when opening/parsing file: {2}".format(e.errno, e.strerror, absoluth_path)
        except:
            print "Unknown error when opening/parsing file: {0}".format(absoluth_path), sys.exc_info()[0]
        finally:
            file.close()

        return file_description

    def __decorate_desription_line(self, line, description_item):
        output_line = description_item

        if line.startswith("(\""):
            line = line.split("(\"", 1)[1]

        if line.endswith("\");"):
            line = line.split("\");", 1)[0]
        elif line.endswith(");"):
            line = line.split(");", 1)[0]

        output_line += ":  " + line
        return output_line

    def __get_test_groups(self, line):
        group_list = []
        groups_str = line[line.find("{") + 1:line.find("}")]
        groups_str_list = groups_str.split(",")
        for group in groups_str_list:
            group = group[group.find(".") + 1:]
            group_list.append(group)

        return group_list

    def do_parsing(self):
        """
        Do parsing for specific folder (path), file extension and list of searching strings
        :param path: path to the start folder
        :param file_extension: file extension for parsing
        :param searching_string_list: list of strings which are searched
        :return: true when parsing successful
        """
        if (self.project_path is None) or (not self.project_path):
            print "Error: Empty folder path for parsing"
            return False
        elif (self.file_extension is None) or (not self.file_extension):
            print "Error: Empty file extension"
            return False

        for path, dirs, files in os.walk(self.project_path):

            if path.endswith(os.sep):
                last_slash_index = path.rfind(os.sep)
                path = path[:last_slash_index]

            actual_directory = path
            second_last_slash = actual_directory.rfind(os.sep)
            actual_directory = actual_directory[second_last_slash + 1:]

            for file in files:
                if file.endswith(self.file_extension):
                    absolute_path = os.path.join(path, file)
                    file_description = self.parsing_java_file(absolute_path, actual_directory, file)
                    self.test_descriptions.append(file_description)
                else:
                    # print "Another file: %s" % file
                    pass

    def create_overview_file(self, file_name):
        """
        Create file and print out parsing overview into this file
        :param file_name:
        :return:
        """
        overview_output = self.__open_file(file_name)
        overview_output.write("--- Parsing path: {0} ---\n\n".format(self.project_path))

        for description in self.test_descriptions:
            self.__print_one_file_overview(overview_output, description)
            overview_output.write(self.__line + "\n\n")

        self.__close_file(overview_output)

    def create_complete_file(self, file_name):
        """
        Create file and print out parsing complete output into this file
        :param file_name:
        :return:
        """
        complete_output = self.__open_file(file_name)
        complete_output.write("--- Parsing path: {0} ---\n\n".format(self.project_path))
        for description in self.test_descriptions:
            self.__print_one_file_overview(complete_output, description)
            for action in description.actionList:
                complete_output.write("{0}\n".format(action))
            complete_output.write(self.__line + "\n\n")

        self.__close_file(complete_output)

    def __open_file(self, file_name):
        try:
            overview_output = open(file_name, "w")
        except IOError as e:
            print "I/O Error(({0}): {1}) when opening output file('%s')!".format(e.errno, e.strerror, file_name)
            return None
        except:
            print "Unknown error when opening output file('%s')!".format(file_name), sys.exc_info()[0]
            return None

        return overview_output

    def __close_file(self, file):
        try:
            file.close()
            return True
        except IOError as e:
            print "I/O Error(({0}): {1}) when closing file('%s')!".format(e.errno, e.strerror, file)
            return False
        except:
            print "Unknown error when closing file('%s')!".format(file), sys.exc_info()[0]
            return False

    def __print_one_file_overview(self, file, file_description):
        file.write("Folder name: {0}\n".format(file_description.folder_name))
        file.write("Package: {0}\n".format(file_description.package))
        file.write("File name: {0}\n".format(file_description.file_name))
        file.write("\n")
        file.write("{0}\n".format(file_description.feature))
        file.write("{0}\n".format(file_description.scenario))
        file.write("{0}\n".format(file_description.given))

    def get_output(self, group):
        """
        Get one long string as test group description
        :param group:
        :return:
        """
        string_output = ""
        if group == constants.ALL_TESTS:
            nmb_tests = 0
            nmb_in_progress_tests = 0
            for test_description in self.test_descriptions:
                one_file_output = self.__format_one_file_output(test_description)
                if isinstance(one_file_output, basestring):
                    string_output += self.__format_one_file_output(test_description)
                    string_output = string_output + self.__line + "\n\n"
                    nmb_tests += 1
                if constants.IN_PROGRESS_TESTS in test_description.test_groups:
                    nmb_in_progress_tests += 1
            test_group_summary = "*** {0} tests in total ({1} in progress tests) ***".format(nmb_tests,
                                                                                             nmb_in_progress_tests)
            test_group_summary += "\n" + self.__line + "\n\n"
            string_output = test_group_summary + string_output

        elif group == constants.SMOKE_TESTS:
            print "SMOKE TESTS PRINTING ..."
            string_output = self.__get_test_group_output(constants.SMOKE_TESTS)
        elif group == constants.REGRESSION_TESTS:
            print "REGRESSION TESTS PRINTING ..."
            string_output = self.__get_test_group_output(constants.REGRESSION_TESTS)
        elif group == constants.RELEASE_TESTS:
            print "RELEASE TESTS PRINTING ..."
            string_output = self.__get_test_group_output(constants.RELEASE_TESTS)
        elif group == constants.ENVIRONMENTAL_TESTS:
            print "ENVIRONMENTAL TESTS PRINTING ..."
            string_output = self.__get_test_group_output(constants.ENVIRONMENTAL_TESTS)
        elif group == constants.EMULATOR_TESTS:
            print "EMULATOR TESTS PRINTING ..."
            string_output = self.__get_test_group_output(constants.EMULATOR_TESTS)
        elif group == constants.IN_PROGRESS_TESTS:
            print "IN PROGRESS TESTS PRINTING ..."
            string_output = self.__get_test_group_output(constants.IN_PROGRESS_TESTS)
        else:
            string_output = "Unknown group"
        return string_output

    def __format_one_file_output(self, test_description):
        """
        Format output for one file
        :return:
        """
        output = "File name: {0}\n".format(test_description.file_name)
        output += "Folder name: {0};\tPackage name: {1}\n".format(test_description.folder_name,
                                                                  test_description.package)
        output += "\t{0}\n\t{1}\n\t{2}\n".format(test_description.feature, test_description.scenario,
                                                 test_description.given)
        return output

    def __get_test_group_output(self, test_group):
        """
        Format output as one string for whole test group
        :param test_group:
        :return:
        """
        string_output = ""
        nmb_tests = 0
        nmb_in_progress_tests = 0
        for test_description in self.test_descriptions:
            if test_group in test_description.test_groups:
                one_file_output = self.__format_one_file_output(test_description)
                if isinstance(one_file_output, basestring):
                    string_output += one_file_output
                    string_output += self.__line + "\n\n"
                    nmb_tests += 1
                if constants.IN_PROGRESS_TESTS in test_description.test_groups:
                    nmb_in_progress_tests += 1
        test_group_summary = "*** {0} tests in {1} group ({2} in progress tests) ***".format(nmb_tests, test_group,
                                                                                             nmb_in_progress_tests)
        test_group_summary += "\n" + self.__line + "\n\n"
        return test_group_summary + string_output
