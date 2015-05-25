import os
import stat
from .output import Output
from time import gmtime, strftime

class FSOperations(object):
    """
    File system operation class describes methods that we use to operate with file system
    """
    def __init__(self):
        self.WORK_DIR = '/mnt/nfs/test_files/'
        self.EXTENSION = '.txt'
        self.DEFAULT_PERMISSIONS_SET = stat.S_IWUSR | stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH
        self.filelist = [f for f in os.listdir(self.WORK_DIR) if f.endswith(self.EXTENSION)]
        self.timestamp = strftime('%Y_%m_%d', gmtime())


    def delete_files(self):
        """
        This method delete all files from our test directory
        :return:
        """
        filelist_delete = self.filelist
        os.chdir(self.WORK_DIR)
        for f in filelist_delete:
            os.remove(f)

    def create_files(self, number):
        """
        This method creates test directory if it does not exists;
        creates custom filename;
        write to created file some meta data
        :param number:
        :return:
        """
        if not os.path.exists(os.path.dirname(self.WORK_DIR)):
            os.makedirs(os.path.dirname(self.WORK_DIR))
        for i in range(number):
            prefix = str(self.timestamp) + '_' + str(i)
            filename = self.WORK_DIR + prefix + self.EXTENSION
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))
            with open(filename, 'w') as f:
                f.write(prefix + '\n')
                f.close()
            os.chmod(filename, self.DEFAULT_PERMISSIONS_SET)

    def get_file_permission(self):
        """
        This method read and print out dictionary
        {filename:permission} for every file in our test directory
        :return:
        """
        dict_perms = {}
        os.chdir(self.WORK_DIR)
        for f in self.filelist:
            permissions = oct(stat.S_IMODE(os.lstat(f).st_mode))
            dict_perms[f] = permissions
        Output().print_result(dict_perms)
        return permissions

    def change_file_permissions(self, permissions):
        """
        This method changes file permissions to custom
        Argument supports only oct numbers.
        Ex: 0444
        :param permissions:
        :return:
        """
        os.chdir(self.WORK_DIR)
        for f in self.filelist:
            os.chmod(f, permissions)
        return oct(permissions)

    def print_files(self):
        """
        This method print file list
        PS: Just in case :)
        :return:
        """
        Output().print_result(self.filelist)