import logging
import os
from ..classes.fs_operations import FSOperations

class Test07(object):

    def test_not_empty_directory(self):
        '''
        This method checks if directory is not empty
        '''
        logging.info('Testing that directory not empty')
        WORK_DIR = '/mnt/nfs/test_files/'
        FSOperations().create_files(5)
        assert os.listdir(WORK_DIR) != []