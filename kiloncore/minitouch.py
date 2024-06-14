from kiloncore import context, consts, utils
import time
from kiloncore.consts import getnowtimeformat
from pyminitouchModify import safe_connection, CommandBuilder
from kiloncore import utils

def tap(template):
    def decorator(func):
        def wrapper(ctx: context.Context):
            if not ctx.is_running:
                exit(0)
            time.sleep(1)
            x, y = utils.whereTemplate(ctx, template)
            if x == -1: 
                return False
            ctx.device.tap([(x, y)])
            func(ctx)
            return True    
        return wrapper
    return decorator

def setTimeOut(ctx: context.Context,func, time = 10):
    for i in range (0, time):
        if func(ctx):
            return True
    print(f"{getnowtimeformat()} 操作超时,请重试...")
    return False

@tap(consts.backHome)
def backHome(ctx: context.Context):
    pass

@tap(consts.startAction)
def starAction(ctx: context.Context):
    pass
    
@tap(consts.memoryActionMode)
def memoryActionMode(ctx: context.Context):
    pass

@tap(consts.enterShow)
def enterShow(ctx: context.Context):
    pass

@tap(consts.recurrence)
def recurrence(ctx: context.Context):
    pass

@tap(consts.actionSuccess)
def actionSuccess(ctx: context.Context):
    pass

@tap(consts.cellActivityDeficiency)
def outcellActivity(ctx: context.Context):
    ctx.device.tap([(0, 0)])

@tap(consts.showResource)
def enterresource(ctx: context.Context):
    pass

@tap(consts.volitionAlanalysis)
def volitionAlanalysis(ctx: context.Context):
    pass

@tap(consts.CoinageAesthetics)
def CoinageAesthetics(ctx: context.Context):
    pass

@tap(consts.HarvestSeason)
def HarvestSeason(ctx: context.Context):
    pass

@tap(consts.DustMovement)
def DustMovement(ctx: context.Context):
    pass

@tap(consts.levelVA)
def volitionAlanalysislevel(ctx: context.Context):
    pass

@tap(consts.levelCA)
def CoinageAestheticslevel(ctx: context.Context):
    pass

@tap(consts.levelHS)
def HarvestSeasonlevel(ctx: context.Context):
    pass

@tap(consts.levelDM)
def DustMovementlevel(ctx: context.Context):
    pass

@tap(consts.selectTime)
def selectTime(ctx: context.Context):
    pass

@tap(consts.x1)
def selectx1(ctx: context.Context):
    pass

@tap(consts.x2)
def selectx2(ctx: context.Context):
    pass

@tap(consts.x3)
def selectx3(ctx: context.Context):
    pass

@tap(consts.x4)
def selectx4(ctx: context.Context):
    pass

@tap(consts.wasteland)
def wasteland(ctx: context.Context):
    pass

@tap(consts.wastelandDialog1)
def wastelandDialog1(ctx: context.Context):
    pass

@tap(consts.wastelandDialog2)
def wastelandDialog2(ctx: context.Context):
    pass

@tap(consts.wastelandHome)
def wastelandHome(ctx: context.Context):
    pass

@tap(consts.wastelandZlce)
def wastelandZlce(ctx: context.Context):
    pass

@tap(consts.wastelandWc)
def wastelandWc(ctx: context.Context):
    pass

@tap(consts.wastelandTrust)
def wastelandTrust(ctx: context.Context):
    pass

@tap(consts.back)
def back(ctx: context.Context):
    pass

@tap(consts.dayweektask)
def enterdayweektask(ctx: context.Context):
    pass

@tap(consts.achieveaward)
def achieveaward(ctx: context.Context):
    pass

@tap(consts.achievemailaward)
def achievemailaward(ctx: context.Context):
    pass

@tap(consts.mail)
def entermail(ctx: context.Context):
    pass

@tap(consts.houhou)
def enterhouhou(ctx: context.Context):
    pass

@tap(consts.weekaward)
def weekaward(ctx: context.Context):
    pass

@tap(consts.dayaward)
def dayaward(ctx: context.Context):
    pass

@tap(consts.receiveAllAward)
def receiveallaward(ctx: context.Context):
    pass

@tap(consts.dwachievesuccess)
def dwachievesuccess(ctx: context.Context):
    pass

@tap(consts.achievehouhouaward)
def achievehouhouaward(ctx: context.Context):
    pass

@tap(consts.hhlevelup)
def hhlevelup(ctx: context.Context):
    pass

@tap(consts.focusaward)
def focusaward(ctx: context.Context):
    pass

@tap(consts.oldhall)
def oldhall(ctx: context.Context):
    pass

@tap(consts.oldhallposition)
def oldhallposition(ctx: context.Context):
    pass

@tap(consts.collectlcze)
def collectlcze(ctx: context.Context):
    pass

@tap(consts.collectwc)
def collectwc(ctx: context.Context):
    pass

@tap(consts.sleepwalk)
def sleepwalk(ctx: context.Context):
    pass

@tap(consts.sleepwalkweekaward)
def sleepwalkweekaward(ctx: context.Context):
    pass

@tap(consts.dsChallenge)
def dsChallenge(ctx: context.Context):
    pass

@tap(consts.dsField)
def dsField(ctx: context.Context):
    pass

@tap(consts.dsTeam)
def dsTeam(ctx: context.Context):
    pass

@tap(consts.dsTeam1)
def dsTeam1(ctx: context.Context):
    pass

@tap(consts.dsTeam2)
def dsTeam2(ctx: context.Context):
    pass

@tap(consts.dsAction)
def dsAction(ctx: context.Context):
    pass

@tap(consts.dsFail)
def dsFail(ctx: context.Context):
    pass


@tap(consts.ds1)
def ds1(ctx: context.Context):
    pass

@tap(consts.ds1Finish)
def ds1Finish(ctx: context.Context):
    pass

@tap(consts.ds2)
def ds2(ctx: context.Context):
    pass

@tap(consts.ds3)
def ds3(ctx: context.Context):
    pass

@tap(consts.ds4)
def ds4(ctx: context.Context):
    pass

@tap(consts.ds5)
def ds5(ctx: context.Context):
    pass

@tap(consts.ds6)
def ds6(ctx: context.Context):
    pass

@tap(consts.ds1Enemy1)
def ds1Enemy1(ctx: context.Context):
    pass

@tap(consts.ds1Enemy2)
def ds1Enemy2(ctx: context.Context):
    pass

@tap(consts.ds2Enemy1)
def ds2Enemy1(ctx: context.Context):
    pass

@tap(consts.ds2Enemy2)
def ds2Enemy2(ctx: context.Context):
    pass

@tap(consts.ds3Enemy1)
def ds3Enemy1(ctx: context.Context):
    pass

@tap(consts.ds3Enemy2)
def ds3Enemy2(ctx: context.Context):
    pass

@tap(consts.ds4Enemy1)
def ds4Enemy1(ctx: context.Context):
    pass

@tap(consts.ds4Enemy2)
def ds4Enemy2(ctx: context.Context):
    pass

@tap(consts.ds5Enemy1)
def ds5Enemy1(ctx: context.Context):
    pass

@tap(consts.ds5Enemy2)
def ds5Enemy2(ctx: context.Context):
    pass

@tap(consts.ds6Enemy1)
def ds6Enemy1(ctx: context.Context):
    pass

@tap(consts.ds6Enemy2)
def ds6Enemy2(ctx: context.Context):
    pass

@tap(consts.dsSpecial)
def dsSpecial(ctx: context.Context):
    pass

@tap(consts.auto)
def auto(ctx: context.Context):
    pass

@tap(consts.speedx1)
def speedx1(ctx: context.Context):
    pass

@tap(consts.dsReset1)
def dsReset1(ctx: context.Context):
    pass

@tap(consts.dsReset2)
def dsReset2(ctx: context.Context):
    pass

@tap(consts.dsReset3)
def dsReset3(ctx: context.Context):
    pass

@tap(consts.dsReset4)
def dsReset4(ctx: context.Context):
    pass

def tapbottom(ctx: context.Context):
    w, h = utils.getWandH(ctx)
    ctx.device.tap([(1/6 * h, 1/2 * w)])

def tapcenter(ctx: context.Context):
    w, h = utils.getWandH(ctx)
    ctx.device.tap([(1/2 * h, 1/2 * w)])

def swipe(ctx: context.Context, x1,y1, x2, y2):
    ctx.device.ext_smooth_swipe([(x1, y1), (x2, y2)],part=10,duration=30)