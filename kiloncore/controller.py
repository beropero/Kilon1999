from kiloncore import minitouch, context
from datetime import datetime

def cmd(ctx: context.Context):
    pass

def getnowtimeformat():
    return datetime.now().strftime("%H:%M:%S")

def setTimeOut(ctx: context.Context,func, time = 10):
    for i in range (0, time):
        if func(ctx) == 0:
            return True
    return False

## 自动重现
def autoRecurrence(ctx: context.Context):    
    minitouch.starAction(ctx)
    
    if not setTimeOut(ctx, minitouch.recurrence):
        print(f"{getnowtimeformat()} 操作超时,请重试...")
        return
        
    if setTimeOut(ctx, minitouch.outcellActivity, 1):
        print(f"{getnowtimeformat()} 细胞活性不足...")
        return

    while minitouch.actionSuccess(ctx) == -1:
        continue
    
    if not setTimeOut(ctx, minitouch.actionSuccess):
        print(f"{getnowtimeformat()} 操作超时,请重试...")
        return

    autoRecurrence(ctx)

## 意志解析
def volitionAlanalysis(ctx: context.Context):
    while minitouch.enterShow(ctx) == -1:
        minitouch.backHome(ctx)
         
    while minitouch.enterresource(ctx) == -1:
        continue
    while minitouch.volitionAlanalysis(ctx) == -1:
        continue

    minitouch.volitionAlanalysislevel(ctx)

    minitouch.starAction(ctx)
    
    while minitouch.memoryActionMode(ctx) == -1:
        continue
   
    minitouch.selectTime(ctx)
  
    minitouch.selectx2(ctx)
      
    while minitouch.recurrence(ctx) == -1:
        continue
    
    if minitouch.outcellActivity(ctx) == 0:
        return

    while minitouch.actionSuccess(ctx) == -1:
        continue

    minitouch.actionSuccess(ctx)

    minitouch.backHome(ctx)

## 收取荒原
def takewasteland(ctx: context.Context):
    while minitouch.wasteland(ctx) == -1:
        minitouch.backHome(ctx)
    
    while minitouch.wastelandHome(ctx) == -1:
       continue
    for i in range(0, 3):
        minitouch.wastelandZlce(ctx)
    minitouch.back(ctx)

    for i in range(0, 3):
        minitouch.wastelandWc(ctx)    
    minitouch.back(ctx)

    minitouch.wastelandTrust(ctx)

    minitouch.backHome(ctx)
