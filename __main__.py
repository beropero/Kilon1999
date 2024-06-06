import sys
from gui import mainwindow
from kiloncore import utils, consts
# 错误处理
def exception_hook(exc_type, exc_value, exc_traceback):
   pass

if __name__ == '__main__':
    sys.excepthook = exception_hook
    mainwindow.Start()
    #utils.getcharfromimage(consts.cellActive)


