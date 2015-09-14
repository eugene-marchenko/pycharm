
import logging
import os
from ..classes.fs_operations import FSOperations

class Test02(object):
    def test_inode_increase(self):
        '''
        This method checks if number of inodes increased when files deleted
        '''
        logging.info('Testing inode increase')
        FSOperations.create_files(1)
        inodes_left = os.statvfs('/mnt/nfs').f_favail
        FSOperations().delete_files()
        assert os.statvfs('/mnt/nfs').f_favail > inodes_left, 'Should be bigger number of inodes'
