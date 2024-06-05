from kiloncore import context, consts, utils
import time
from kiloncore.consts import getnowtimeformat

def tap(template):
    def decorator(func):
        def wrapper(ctx: context.Context):
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

@tap(consts.levelVA)
def volitionAlanalysislevel(ctx: context.Context):
    pass

@tap(consts.selectTime)
def selectTime(ctx: context.Context):
    pass

@tap(consts.x2)
def selectx2(ctx: context.Context):
    pass

@tap(consts.wasteland)
def wasteland(ctx: context.Context):
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

def swipe(ctx: context.Context, x1,y1, x2, y2):
    ctx.device.swipe([(x1, y1), (x2, y2)])
