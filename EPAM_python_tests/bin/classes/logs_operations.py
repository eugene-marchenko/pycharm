import os
from time import gmtime, strftime

class LogsOperations(object):
    def __init__(self):
        self.WORK_DIR = 'logs/'
        self.EXTENSION = '.log'
        self.timestamp = strftime('%Y%m%d_%H%M%S', gmtime())

    def delete_logs(self):
        filelist = [f for f in os.listdir(self.WORK_DIR) if f.endswith(self.EXTENSION)]
        current_dir = os.getcwd()
        for f in filelist:
            os.chdir(self.WORK_DIR)
            os.remove(f)
            os.chdir(current_dir)

    def create_dir_and_log_file(self):
        print os.getcwd()
        if not os.path.exists(os.path.dirname(self.WORK_DIR)):
            os.makedirs(os.path.dirname(self.WORK_DIR))
        filename = self.WORK_DIR + str(self.timestamp) + self.EXTENSION
        if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
        return filename
