import sys
import os
from gui import mainwindow

# 错误处理
def exception_hook(exc_type, exc_value, exc_traceback):
   pass

if __name__ == '__main__':
   sys.excepthook = exception_hook
   
   mainwindow.Start()


