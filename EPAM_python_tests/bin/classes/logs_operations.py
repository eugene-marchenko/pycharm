import os
import pytest
from time import gmtime, strftime

class LogsOperations(object):
    """
    This class describes methods to operate with log files
    """
    def __init__(self):
        self.WORK_DIR = 'logs/'
        self.EXTENSION = '.log'
        self.timestamp = strftime('%Y%m%d_%H%M%S', gmtime())

    def delete_logs(self):
        """
        This method deletes all logs from log directory
        :return:
        """
        if os.path.isdir(self.WORK_DIR):
            filelist = [f for f in os.listdir(self.WORK_DIR) if f.endswith(self.EXTENSION)]
            current_dir = os.getcwd()
            for f in filelist:
                os.chdir(self.WORK_DIR)
                os.remove(f)
                os.chdir(current_dir)

    def create_dir_and_log_file(self, class_name):
        """
        This method creates new directory(if does not exists) and log file with custom filename
        :param class_name:
        :return:
        """
        print os.getcwd()
        if not os.path.exists(os.path.dirname(self.WORK_DIR)):
            os.makedirs(os.path.dirname(self.WORK_DIR))
        filename = self.WORK_DIR + str(self.timestamp) + '_' + class_name + self.EXTENSION
        return filename

    def test_class(self, filename):
        """
        This method runs pytests to test functionality of our main classes
        :param filename:
        :return:
        """
        file_specifier = filename.split('/', 1)[1].split('.', 1)[0]
        pytest.main(filename + ' --resultlog=%s' % self.create_dir_and_log_file(file_specifier))
