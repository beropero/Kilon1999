from core import minitouch, context

## 自动重现
def autoRecurrence(ctx: context.Context):    
    minitouch.starAction(ctx)
   
    while minitouch.recurrence(ctx) == -1:
        continue
    
    if minitouch.outcellActivity(ctx) == 0:
        return

    while minitouch.actionSuccess(ctx) == -1:
        continue
    
    minitouch.actionSuccess(ctx)

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
