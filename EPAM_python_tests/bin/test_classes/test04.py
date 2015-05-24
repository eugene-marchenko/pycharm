import logging
import os
from ..classes.fs_operations import FSOperations

class Test04(object):

    def test_inode_decrease(self):
        '''
        This method checks if number of inodes decrease if new files created
        '''
        logging.info('Testing inode decrease')
        inodes_left = os.statvfs('/mnt/nfs').f_favail
        FSOperations().create_files(20)
        assert os.statvfs('/mnt/nfs').f_favail <= inodes_left, 'Should be less number of inodes'