from kiloncore import minitouch, context
from kiloncore.consts import getnowtimeformat
from kiloncore.minitouch import setTimeOut
from kiloncore.task import WastelandTask, VolitionalAnalysisTask, AchieveAwardTask,CellActiveTask
import time
from typing import List
from kiloncore.task import Task

def cmd(ctx: context.Context):
    tasklist:  List[Task]= [
        CellActiveTask(ctx),
        VolitionalAnalysisTask(ctx),
        WastelandTask(ctx), 
        AchieveAwardTask(ctx),
    ]    

    for i in tasklist:
        i.execute()

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
