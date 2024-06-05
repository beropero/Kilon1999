from abc import abstractmethod, ABCMeta
from kiloncore import minitouch
from kiloncore.minitouch import setTimeOut
from kiloncore import context
from kiloncore.consts import getnowtimeformat

class Tack(metaclass=ABCMeta):
    ## 执行步骤
    @abstractmethod
    def process(self):
        pass

    ## 开始执行
    @abstractmethod
    def execute(self):
        pass

# 荒原收取任务
class WastelandTack(Tack):
    def __init__(self, ctx: context.Context):
        self.ctx = ctx
    
    ## 进入荒原
    def EnterWasteland(self, ctx):
        if not minitouch.wasteland(self.ctx):
            minitouch.backHome(self.ctx)
            return False
        return True

    ## 收取智利齿儿
    def CollecWastelandtZlce(self):
        for i in range(0, 3):
            minitouch.wastelandZlce(self.ctx)
        minitouch.back(self.ctx)
    
    ## 收取微尘
    def CollecWastelandtWc(self):
        for i in range(0, 3):
            minitouch.wastelandWc(self.ctx)    
        minitouch.back(self.ctx)

    def process(self):
        setTimeOut(self.ctx, self.EnterWasteland)
    
        setTimeOut(self.ctx, minitouch.wastelandHome)
       
        self.CollecWastelandtZlce()

        self.CollecWastelandtWc()

        ## 收取信赖
        minitouch.wastelandTrust(self.ctx)

        ## 返回主页
        minitouch.backHome(self.ctx)

    def execute(self):
        if not self.ctx.conf['Wasteland']['check']:
            return
        print(f"{getnowtimeformat()} 荒原收取")
        self.process()