import stat
import os

print os.statvfs('/mnt/nfs').f_favail