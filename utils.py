import cv2
import numpy as np
import context
import adb
import consts

# 图片模板寻址
def whereTemplate(ctx: context.Context,template_path):
    adb.screencap(ctx)

    src = cv2.imread(consts.screencap, cv2.IMREAD_GRAYSCALE)

    # 加载模板图像
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    # 确保模板图像小于源图像
    if src.shape[:2] < template.shape[:2]:
        print("模板图像应小于源图像")
        exit(1)

    # 计算模板的宽度和高度
    w, h = template.shape[::-1]
    sw, sh = src.shape[::-1]
    # 进行模板匹配
    res = cv2.matchTemplate(src, template, cv2.TM_CCOEFF_NORMED)
    
    # 设置阈值
    threshold = 0.8
    
    # 找到匹配的位置
    loc = np.where(res >= threshold)
    if len(loc[0]) == 0 or len(loc[1]) == 0:
        return -1, -1
    x = loc[1][0] + 1/2 * w
    y = loc[0][0] + 1/2 * h

    return sh - y, x



