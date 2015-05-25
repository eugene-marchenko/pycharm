from .classes.fs_operations import FSOperations

'''
Prepare environment
'''

FSOperations().delete_files()
FSOperations().create_files(5)
FSOperations().get_file_permission()
FSOperations().change_file_permissions(0o0777)
FSOperations().get_file_permission()

