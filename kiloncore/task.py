from abc import abstractmethod, ABCMeta
from kiloncore import minitouch
from kiloncore.minitouch import setTimeOut
from kiloncore import context
from kiloncore.consts import getnowtimeformat
from kiloncore import utils, consts
import time

class Task(metaclass=ABCMeta):
    ## 执行步骤
    @abstractmethod
    def process(self):
        pass

    ## 开始执行
    @abstractmethod
    def execute(self):
        pass

# 刷活性任务
class CellActiveTask(Task):
    def __init__(self, ctx: context.Context):
        self.ctx = ctx
        self.Time = self.ctx.conf['CellActive']['time']
        self.Check = self.ctx.conf['CellActive']['check']
        self.level = self.ctx.conf['CellActive']['levelselect']
        self.nextlevel = self.ctx.conf['CellActive']['nextlevels']
    # 进入show
    def EnterShow(self, ctx):
        if not minitouch.enterShow(self.ctx):
            minitouch.backHome(self.ctx)
            return False
        return True

    # 进入关卡
    def Enterlevel(self, func1, func2):
        if not setTimeOut(self.ctx, self.EnterShow):
            return
        minitouch.enterresource(self.ctx)
        if not func1(self.ctx):
            w, h = utils.getWandH(self.ctx)
            for i in range(0, 3):
                minitouch.swipe(self.ctx, 1/2*h, 2/3*w, 1/2*h, 1/3*w)
                time.sleep(1)
            func1(self.ctx)
        func2(self.ctx)

        minitouch.starAction(self.ctx)

    # 一次复现
    def recurrence(self):
        if not setTimeOut(self.ctx, minitouch.recurrence):
            exit(0)
        if not setTimeOut(self.ctx, minitouch.actionSuccess, 300):
            exit(0)
        time.sleep(1)
        minitouch.actionSuccess(self.ctx)
    
    # 活性复现
    def cellactivetime(self):
        if self.Time == 0:
            return
        minitouch.memoryActionMode(self.ctx)

        minitouch.selectTime(self.ctx)
        minitouch.selectx1(self.ctx)

        self.oneactive = self.onetimehowmach()
        if self.oneactive == 0:
            print(f"{getnowtimeformat()} 活性不足")
            return

        flag, self.lastactive = utils.residualActivity(self.ctx)
        if flag:
            print(f"{getnowtimeformat()} 剩余活性:{self.lastactive}")

            if self.lastactive < self.oneactive:
                print(f"{getnowtimeformat()} 活性不足")
                return

            idealactive = self.Time * self.oneactive

            active = idealactive if idealactive < self.lastactive else self.lastactive

            # 复现x1次数
            x1time = int(active/self.oneactive)

            # 复现x4次数
            x4time = int(x1time/4)

            # 剩余复现次数
            surplustime = x1time%4

            # 开始复现
            if x4time > 0:
                minitouch.selectTime(self.ctx)
                minitouch.selectx4(self.ctx)
                for i in range(0, x4time):
                    self.recurrence()
                    self.lastactive -= 4 * self.oneactive
                    print(f"{getnowtimeformat()} 4级复现 x {i+1}")
                    print(f"{getnowtimeformat()} 剩余活性:{self.lastactive}")

                time.sleep(4)

            if surplustime > 0:
                minitouch.selectTime(self.ctx)
                select = getattr(minitouch, f"selectx{surplustime}")
                select(self.ctx)
                self.recurrence()
                self.lastactive -= surplustime * self.oneactive
                print(f"{getnowtimeformat()} {surplustime}级复现 x 1")
                print(f"{getnowtimeformat()} 剩余活性:{self.lastactive}")

                time.sleep(4) 

    # 读取一次多少活性
    def onetimehowmach(self):
        flag, active = utils.howMachActive(self.ctx)
        if flag and active!=0:
            print(f"{getnowtimeformat()} 关卡活性:{active}")
        return active

    def process(self):
        if self.level == 0:
            minitouch.starAction(self.ctx)
            time.sleep(4)
            self.cellactivetime()
        if self.level == 1:
            self.Enterlevel(minitouch.CoinageAesthetics, minitouch.CoinageAestheticslevel)
            time.sleep(4)
            self.cellactivetime()
        elif self.level == 2:
            self.Enterlevel(minitouch.DustMovement, minitouch.DustMovementlevel)
            time.sleep(4)
            self.cellactivetime()
        elif self.level == 3:
            self.Enterlevel(minitouch.HarvestSeason, minitouch.HarvestSeasonlevel)
            time.sleep(4)
            self.cellactivetime()

        # 剩余理智
        if self.nextlevel == 0:
            return
        self.Time = 999
        if self.nextlevel == 1:
            self.Enterlevel(minitouch.CoinageAesthetics, minitouch.CoinageAestheticslevel)
            time.sleep(4)
            self.cellactivetime()
        elif self.nextlevel == 2:
            self.Enterlevel(minitouch.DustMovement, minitouch.DustMovementlevel)
            time.sleep(4)
            self.cellactivetime()
        elif self.nextlevel == 3:
            self.Enterlevel(minitouch.HarvestSeason, minitouch.HarvestSeasonlevel)
            time.sleep(4)
            self.cellactivetime()

    def execute(self):
        if not self.Check or (self.Time == 0 and self.nextlevel == 0):
            return
        print(f"{getnowtimeformat()} 刷活性")
        self.process()
        time.sleep(5)
    
# 意志解析任务
class VolitionalAnalysisTask(Task):
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
            exit(0)
        minitouch.enterresource(self.ctx)
        if not minitouch.volitionAlanalysis(self.ctx):
            w, h = utils.getWandH(self.ctx)
            for i in range(0, 3):
                minitouch.swipe(self.ctx, 1/2*h, 2/3*w, 1/2*h, 1/3*w)
                time.sleep(1)
            minitouch.volitionAlanalysis(self.ctx)
        minitouch.volitionAlanalysislevel(self.ctx)

        minitouch.starAction(self.ctx)

    # 一次复现
    def recurrence(self):
        if not setTimeOut(self.ctx, minitouch.recurrence):
            exit(0)
        if not setTimeOut(self.ctx, minitouch.actionSuccess, 300):
            exit(0)
        time.sleep(1)
        minitouch.actionSuccess(self.ctx)

    # 深度解析
    def depthtime(self):
        if self.Time == 0:
            return
        self.EnterVolitionalAnalysis()
        time.sleep(4)
        minitouch.memoryActionMode(self.ctx)
        x, _ = utils.whereTemplate(self.ctx, consts.depthanalysis)
        if x != -1:
            flag, depth = utils.residualAnalysis(self.ctx)
            if flag:
                print(f"{getnowtimeformat()} 深度解析:{depth}/2")
                if self.Time >= 2:
                    self.Time -= depth
                    rt = depth if self.Time < depth else self.Time
                    minitouch.selectTime(self.ctx)
                    select = getattr(minitouch, f"selectx{rt}")
                    select(self.ctx)
                    self.recurrence()
    
    # 活性复现
    def cellactivetime(self):
        if self.Time == 0:
            return
        minitouch.memoryActionMode(self.ctx)
        minitouch.selectTime(self.ctx)
        minitouch.selectx1(self.ctx)

        self.oneactive = self.onetimehowmach()

        if self.oneactive == 0:
            print(f"{getnowtimeformat()} 活性不足")
            return

        flag, self.lastactive = utils.residualActivity(self.ctx)
        if flag:
            print(f"{getnowtimeformat()} 剩余活性:{self.lastactive}")

            if self.lastactive < self.oneactive:
                print(f"{getnowtimeformat()} 活性不足")
                return

            idealactive = self.Time * self.oneactive

            active = idealactive if idealactive < self.lastactive else self.lastactive

            # 复现x1次数
            x1time = int(active/self.oneactive)

            # 复现x4次数
            x4time = int(x1time/4)

            # 剩余复现次数
            surplustime = x1time%4

            # 开始复现
            if x4time > 0:
                minitouch.selectTime(self.ctx)
                minitouch.selectx4(self.ctx)
                for i in range(0, x4time):
                    self.recurrence()
                    self.lastactive -= 4 * self.oneactive
                    print(f"{getnowtimeformat()} 4级复现 x {i+1}")
                    print(f"{getnowtimeformat()} 剩余活性:{self.lastactive}")

                time.sleep(4)

            if surplustime > 0:
                minitouch.selectTime(self.ctx)
                select = getattr(minitouch, f"selectx{surplustime}")
                select(self.ctx)
                self.recurrence()
                self.lastactive -= surplustime * self.oneactive
                print(f"{getnowtimeformat()} {surplustime}级复现 x 1")
                print(f"{getnowtimeformat()} 剩余活性:{self.lastactive}")

                time.sleep(4)

    # 读取一次多少活性
    def onetimehowmach(self):
        flag, active = utils.howMachActive(self.ctx)
        if flag and active != 0:
            print(f"{getnowtimeformat()} 关卡活性:{active}")
        return active

    def process(self):
        self.depthtime()

        self.cellactivetime()    

    def execute(self):
        if not self.Check or self.Time == 0:
            return
        print(f"{getnowtimeformat()} 意志解析")
        self.process()
        time.sleep(5)


# 荒原收取任务
class WastelandTask(Task):
    def __init__(self, ctx: context.Context):
        self.ctx = ctx
    
    ## 进入荒原
    def EnterWasteland(self, ctx):
        if not minitouch.wasteland(self.ctx):
            minitouch.backHome(self.ctx)
            return False
        return True

    def process(self):
        if not setTimeOut(self.ctx, self.EnterWasteland):
            exit(0)

        if not setTimeOut(self.ctx, minitouch.oldhallposition):
            exit(0)

        minitouch.oldhall(self.ctx)

        minitouch.collectwc(self.ctx)
        # 收取利齿子儿
        minitouch.collectlcze(self.ctx)
        # 收取微尘
        minitouch.back(self.ctx)

        ## 收取信赖
        minitouch.wastelandTrust(self.ctx)

        ## 返回主页
        minitouch.backHome(self.ctx)

    def execute(self):
        if not self.ctx.conf['Wasteland']['check']:
            return
        print(f"{getnowtimeformat()} 荒原收取")
        self.process()
        time.sleep(5)


class AchieveAwardTask:
    def __init__(self, ctx: context.Context):
        self.ctx = ctx
        self.dayAndWeek = self.ctx.conf['AchieveAward']['dayAndWeek']
        self.mail = self.ctx.conf['AchieveAward']['mail']
        self.hhJukebox = self.ctx.conf['AchieveAward']['hhJukebox']

    def AchieveDayAndWeekAward(self):
        if not setTimeOut(self.ctx, minitouch.enterdayweektask):
            exit(0)

        if not setTimeOut(self.ctx, minitouch.dayaward):
            exit(0)

        if minitouch.receiveallaward(self.ctx):
            time.sleep(3)
            minitouch.tapbottom(self.ctx)
        if minitouch.achieveaward(self.ctx):
            time.sleep(3)
            minitouch.tapbottom(self.ctx)

        if not setTimeOut(self.ctx, minitouch.weekaward):
            exit(0)

        if minitouch.receiveallaward(self.ctx):
            time.sleep(3)
            minitouch.tapbottom(self.ctx)
        if minitouch.achieveaward(self.ctx):
            time.sleep(3)
            minitouch.tapbottom(self.ctx)
    
    def Achievehhaward(self):
        if not setTimeOut(self.ctx, minitouch.enterhouhou):
            exit(0)
        if minitouch.achievehouhouaward(self.ctx):
            time.sleep(3)
            minitouch.tapbottom(self.ctx)
        minitouch.focusaward(self.ctx)
        if minitouch.achievehouhouaward(self.ctx):
            time.sleep(3)
            minitouch.tapbottom(self.ctx)

    def AchieveMailAward(self):
        if not setTimeOut(self.ctx, minitouch.entermail):
            exit(0)
        minitouch.achievemailaward(self.ctx)
        time.sleep(3)
        minitouch.tapbottom(self.ctx)

    def process(self):
        minitouch.backHome(self.ctx)
        minitouch.tapcenter(self.ctx)
        if self.dayAndWeek:
            print(f"{getnowtimeformat()} 任务")
            self.AchieveDayAndWeekAward()
            minitouch.backHome(self.ctx)
        if self.mail:
            print(f"{getnowtimeformat()} 邮件")
            self.AchieveMailAward()
            minitouch.back(self.ctx)
        if self.hhJukebox:
            print(f"{getnowtimeformat()} 点唱机")
            self.Achievehhaward()
            minitouch.backHome(self.ctx)

    def execute(self):
        if not self.ctx.conf['AchieveAward']['check']:
            return
        print(f"{getnowtimeformat()} 奖励领取")
        self.process()
        time.sleep(5)

# 人工梦游任务
class SleepWalkTask(Task):
    def __init__(self, ctx: context.Context):
        self.ctx = ctx
        self.Check = self.ctx.conf['Sleepwalk']['check']
    
    # 进入show
    def EnterShow(self, ctx):
        if not minitouch.enterShow(self.ctx):
            minitouch.backHome(self.ctx)
            return False
        return True
    
    # 进入深眠域
    def enterdepthsleep(self,ctx):
        if not minitouch.dsField(self.ctx):
            minitouch.sleepwalkweekaward(self.ctx)
            minitouch.dsChallenge(self.ctx)
            return False
        return True
    # 选择队伍
    def selectteam(self, ctx):
        if not self.teamfunc(self.ctx):
            minitouch.dsTeam(self.ctx)
            return False
        return True
    
    # 返回深眠域
    def backdsfield(self, ctx):
        if not minitouch.dsField(self.ctx):
            minitouch.back(self.ctx)
            return False
        return True
    # 一次战斗
    def battle(self, func):
        self.teamfunc = func
        if not setTimeOut(self.ctx, self.selectteam):
            exit(0)

        minitouch.dsAction(self.ctx)

        for i in range (0, 10):
            if minitouch.dsSpecial(self.ctx):
                if not setTimeOut(self.ctx, minitouch.auto):
                    exit(0)
                minitouch.speedx1(self.ctx)

        if not minitouch.setTimeOut(self.ctx, minitouch.actionSuccess, 600):
            exit(0)

        minitouch.actionSuccess(self.ctx)

    # 重置梦境
    def reset(self):
        if not setTimeOut(self.ctx, minitouch.dsReset1):
            exit(0)
        time.sleep(1)
        minitouch.dsReset2(self.ctx)
        minitouch.dsReset3(self.ctx)
        if minitouch.dsReset4(self.ctx):
            return
        if not setTimeOut(self.ctx, minitouch.back):
            exit(0)
    # 深眠单片段流程
    def ds(self, i: int):
        if not setTimeOut(self.ctx, getattr(minitouch, f"ds{i}")):
            exit(0)
        
        self.reset()

        if not setTimeOut(self.ctx, getattr(minitouch, f"ds{i}Enemy1")):
            exit(0)
        self.battle(minitouch.dsTeam1)

        if not setTimeOut(self.ctx, getattr(minitouch, f"ds{i}Enemy2")):
            exit(0)
        self.battle(minitouch.dsTeam2)

        if not setTimeOut(self.ctx, self.backdsfield):
            exit(0)
    def process(self):
        levelname = ["深眠片段·Ⅰ","深眠片段·Ⅱ","深眠片段·Ⅲ","深眠片段·Ⅳ","深眠片段·Ⅴ","深眠片段·Ⅵ"]
        if not setTimeOut(self.ctx, self.EnterShow):
            exit(0)
        minitouch.sleepwalk(self.ctx)
        if not setTimeOut(self.ctx, self.enterdepthsleep):
            exit(0)
        # 滑动至最左
        time.sleep(2)
        w, h = utils.getWandH(self.ctx)
        for i in range(0, 3):
            minitouch.swipe(self.ctx, 1/2*h, 1/3*w, 1/2*h, 2/3*w)
            time.sleep(1)

        for i in range (1, 7):
            if i == 4:
                # 滑动至最右
                for j in range(0, 3):
                    minitouch.swipe(self.ctx, 1/2*h, 2/3*w, 1/2*h, 1/3*w)
                    time.sleep(1)

            print(f"{getnowtimeformat()} {levelname[i-1]}")

            self.ds(i)

    def execute(self):
        if not self.Check:
            return
        print(f"{getnowtimeformat()} 人工梦游")
        self.process()
        time.sleep(5)
