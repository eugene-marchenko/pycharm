import logging
import os
from ..classes.fs_operations import FSOperations

class Test06(object):

    def test_empty_file(self):
        '''
        This method checks if file is not empty
        '''
        logging.info('Testing empty file')
        WORK_DIR = '/mnt/nfs/test_files/'
        FSOperations().create_files(5)
        filelist = [f for f in os.listdir(WORK_DIR) if f.endswith('.txt')]
        os.chdir(WORK_DIR)
        assert os.stat(filelist[0]).st_size != 0, 'Should be not empty'