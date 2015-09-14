from classes.logs_operations import LogsOperations

'''
Run tests
'''

LogsOperations().delete_logs()
LogsOperations().test_class('test_classes/test01.py')
LogsOperations().test_class('test_classes/test02.py')
LogsOperations().test_class('test_classes/test03.py')
LogsOperations().test_class('test_classes/test04.py')
LogsOperations().test_class('test_classes/test05.py')
LogsOperations().test_class('test_classes/test06.py')
LogsOperations().test_class('test_classes/test07.py')
