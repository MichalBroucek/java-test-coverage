__author__ = 'brouk'


class TestDescription:
    """
    Description items of one test
    """

    def __init__(self):
        self.package = ""
        self.folder_name = ""
        self.file_name = ""
        self.test_groups = []
        self.feature = ""
        self.scenario = ""
        self.given = ""
        self.actionList = []

    @property
    def is_complete(self):
        """
        :return:
        """
        if self.package and self.folder_name and self.file_name and \
                self.feature and self.scenario and self.given and \
                self.actions and self.test_groups:
            return True
        else:
            return False


    def to_list(self):
        return [self.package, self.folder_name, self.file_name, self.test_groups, self.feature, self.scenario, self.given, self.actionList]


    def to_string(self):
        return "{0}".format(self.to_list())
