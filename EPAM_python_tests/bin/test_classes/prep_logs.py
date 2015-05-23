import logging

class PrepLogs(object):
    def logAssert(self, test, msg):
        if not test:
            logging.error(msg)
            assert test, msg
