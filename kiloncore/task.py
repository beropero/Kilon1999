from abc import abstractmethod, ABCMeta
from kiloncore import minitouch
from kiloncore.minitouch import setTimeOut
from kiloncore import context
from kiloncore.consts import getnowtimeformat
from kiloncore import utils
import time

class Tack(metaclass=ABCMeta):
    ## 执行步骤
    @abstractmethod
    def process(self):
        pass

    ## 开始执行
    @abstractmethod
    def execute(self):
        pass
    
# 意志解析任务
class VolitionalAnalysisTask(Tack):
    def __init__(self, ctx: context.Context):
        self.ctx = ctx
        self.Time = self.ctx.conf['VolitionalAnalysis']['time']
        self.Check = self.ctx.conf['VolitionalAnalysis']['check']

    # 进入show
    def EnterShow(self, ctx):
        if not minitouch.enterShow(self.ctx):
            minitouch.backHome(self.ctx)
            return False
        return True

    # 进入意志解析
    def EnterVolitionalAnalysis(self):
        if not setTimeOut(self.ctx, self.EnterShow):
            return
        minitouch.enterresource(self.ctx)
        minitouch.enterresource(self.ctx)
        if not minitouch.volitionAlanalysis(self.ctx):
            w, h = utils.getWandH(self.ctx)
            for i in range(0, 3):
                minitouch.swipe(self.ctx, 1/2*h, 2/3*w, 1/2*h, 1/3*w)
                time.sleep(1)
            minitouch.volitionAlanalysis(self.ctx)
        minitouch.volitionAlanalysislevel(self.ctx)

    def process(self):
        self.EnterVolitionalAnalysis()

    def execute(self):
        if not self.Check or self.Time == 0:
            return
        print(f"{getnowtimeformat()} 意志解析")
        self.process()


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
        if not setTimeOut(self.ctx, self.EnterWasteland):
            return
    
        if not setTimeOut(self.ctx, minitouch.wastelandHome):
            return
       
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


class AchieveAwardTask:
    def __init__(self, ctx: context.Context):
        self.ctx = ctx
        self.dayAndWeek = self.ctx.conf['AchieveAward']['dayAndWeek']
        self.mail = self.ctx.conf['AchieveAward']['mail']
        self.hhJukebox = self.ctx.conf['AchieveAward']['hhJukebox']

    def AchieveDayAndWeekAward(self):
        minitouch.enterdayweektask(self.ctx)
        if minitouch.receiveallaward(self.ctx):
            time.sleep(3)
            minitouch.tapbottom(self.ctx)
        if minitouch.achieveaward(self.ctx):
            time.sleep(3)
            minitouch.tapbottom(self.ctx)
        minitouch.weekaward(self.ctx)
        if minitouch.receiveallaward(self.ctx):
            time.sleep(3)
            minitouch.tapbottom(self.ctx)
        if minitouch.achieveaward(self.ctx):
            time.sleep(3)
            minitouch.tapbottom(self.ctx)
    
    def Achievehhaward(self):
        minitouch.enterhouhou(self.ctx)
        if minitouch.achievehouhouaward(self.ctx):
            time.sleep(3)
            minitouch.tapbottom(self.ctx)
        minitouch.focusaward(self.ctx)
        if minitouch.achievehouhouaward(self.ctx):
            time.sleep(3)
            minitouch.tapbottom(self.ctx)

    def AchieveMailAward(self):
        minitouch.entermail(self.ctx)
        minitouch.achievemailaward(self.ctx)
        time.sleep(3)
        minitouch.tapbottom(self.ctx)

    def process(self):
        minitouch.backHome(self.ctx)
        if self.dayAndWeek:
            self.AchieveDayAndWeekAward()
            minitouch.backHome(self.ctx)
        if self.mail:
            self.AchieveMailAward()
            minitouch.back(self.ctx)
        if self.hhJukebox:
            self.Achievehhaward()
            minitouch.backHome(self.ctx)

    def execute(self):
        if not self.ctx.conf['AchieveAward']['check']:
            return
        print(f"{getnowtimeformat()} 奖励领取")
        self.process()
