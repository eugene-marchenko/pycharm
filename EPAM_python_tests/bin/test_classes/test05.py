import logging
import os
from ..classes.fs_operations import FSOperations

class Test05(object):

    def test_empty_directory(self):
        '''
        This method checks if directory is empty
        '''
        logging.info('Testing that directory empty')
        WORK_DIR = '/mnt/nfs/test_files/'
        FSOperations().delete_files()
        assert os.listdir(WORK_DIR) == []