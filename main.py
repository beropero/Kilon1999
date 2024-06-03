from core import context, controller

if __name__ == '__main__':

    ## 初始化上下文
    ctx = context.Context()

    controller.takewasteland(ctx)

    ctx.Close()

