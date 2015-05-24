import logging
import os
from ..classes.fs_operations import FSOperations

class Test03(object):

    def test_number_of_created_files(self):
        logging.info('Testing number of created files')
        FSOperations().delete_files()
        FSOperations().create_files(2)
        WORK_DIR = '/mnt/nfs/test_files/'
        filelist = [f for f in os.listdir(WORK_DIR) if f.endswith('.txt')]
        assert len(filelist) == 2, 'Should be equal to 2'