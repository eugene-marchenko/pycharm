import pytest
from test_classes.prep_logs import *
from classes.logs_operations import LogsOperations
from test_classes.test01 import Test01

LogsOperations().delete_logs()

logging.basicConfig(filename=LogsOperations().create_dir_and_log_file(), level=logging.INFO)
logging.info('start')
# pytest.main('test_classes/prep_logs.py')
pytest.main(Test01().test_foo())
pytest.main(Test01().test_foobar())
logging.info('done')