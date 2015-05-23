import os
import stat

class FileOperations(object):
    def __init__(self):
        self.WORK_DIR = '/mnt/nfs/test_files/'
        self.DEFAULT_PERMISSIONS_SET = stat.S_IWUSR | stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH

    def delete_files(self):
        filelist_delete = [f for f in os.listdir(self.WORK_DIR) if f.endswith('.txt')]
        for f in filelist_delete:
            os.chdir(self.WORK_DIR)
            os.remove(f)

    def create_files(self, number):
        if not os.path.exists(os.path.dirname(self.WORK_DIR)):
            os.makedirs(os.path.dirname(self.WORK_DIR))
        from time import gmtime, strftime
        timestamp = strftime('%Y%m%d_%H%M%S', gmtime())
        for i in xrange(number):
            prefix = str(timestamp) + '_' + str(i)
            filename = self.WORK_DIR + prefix + '.txt'
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            with open(filename, 'w') as f:
                f.write(prefix + '\n')
                f.close()
            os.chmod(filename, self.DEFAULT_PERMISSIONS_SET)