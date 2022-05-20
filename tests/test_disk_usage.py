import os
from disk_report import get_size
#../BASH_DISK_USAGE_PROJECT/aa         1          4     169293
#../BASH_DISK_USAGE_PROJECT/aa/bb         2          4  121023


path= '../BASH_DISK_USAGE_PROJECT/aa/bb'



def test_get_size():
    
    total,numfiles,numSubs= get_size(path)
    
    assert total == 121023
    assert numSubs == 2
    assert numfiles == 4
    