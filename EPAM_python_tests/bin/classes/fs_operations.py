import os
import stat
from output import Output
from time import gmtime, strftime


class FSOperations(object):
    def __init__(self):
        self.WORK_DIR = '/mnt/nfs/test_files/'
        self.EXTENSION = '.txt'
        self.DEFAULT_PERMISSIONS_SET = stat.S_IWUSR | stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH
        self.filelist = [f for f in os.listdir(self.WORK_DIR) if f.endswith(self.EXTENSION)]
        self.timestamp = strftime('%Y_%m_%d', gmtime())


    def delete_files(self):
        filelist_delete = self.filelist
        os.chdir(self.WORK_DIR)
        for f in filelist_delete:
            os.remove(f)

    def create_files(self, number):
        if not os.path.exists(os.path.dirname(self.WORK_DIR)):
            os.makedirs(os.path.dirname(self.WORK_DIR))
        for i in xrange(number):
            prefix = str(self.timestamp) + '_' + str(i)
            filename = self.WORK_DIR + prefix + self.EXTENSION
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            with open(filename, 'w') as f:
                f.write(prefix + '\n')
                f.close()
            os.chmod(filename, self.DEFAULT_PERMISSIONS_SET)

    def get_file_permission(self):
        dict_perms = {}
        os.chdir(self.WORK_DIR)
        for f in self.filelist:
            permissions = oct(stat.S_IMODE(os.lstat(f).st_mode))
            dict_perms[f] = permissions
        Output().print_result(dict_perms)

    def change_file_permissions(self, permissions):
        os.chdir(self.WORK_DIR)
        for f in self.filelist:
            os.chmod(f, permissions)