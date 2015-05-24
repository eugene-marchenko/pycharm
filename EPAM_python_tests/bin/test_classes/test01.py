import logging
from ..classes.fs_operations import FSOperations

class Test01(object):
    # def logAssert(self, test, msg):
    #     if not test:
    #         logging.error(msg)
    #         assert test, msg

    def test_change_file_permissions(self):
        logging.info('Testing file permissions change')
        assert FSOperations().change_file_permissions(0444) == FSOperations().get_file_permission(), \
            'Should return permissions 0444'
        FSOperations().change_file_permissions(0644)
