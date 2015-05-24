import logging
import os
from ..classes.fs_operations import FSOperations

class Test02(object):

    def test_inode_decrease(self):
        logging.info('Testing inode decrease')
        inodes_left = os.statvfs('/mnt/nfs').f_favail
        FSOperations().create_files(20)
        assert os.statvfs('/mnt/nfs').f_favail <= inodes_left, 'Should be less number of inodes'