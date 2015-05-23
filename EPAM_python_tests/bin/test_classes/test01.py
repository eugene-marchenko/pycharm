import logging
from prep_logs import PrepLogs

class Test01(object):
    def test_foo(self):
        logging.info('testing foo')
        PrepLogs().logAssert('foo' == 'foo', 'FAILED: foo is not foo')

    def test_foobar(self):
        logging.info('testing foobar')
        PrepLogs().logAssert('foobar' == 'foo', 'FAILED: foobar is not foo')