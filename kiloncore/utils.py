import cv2
import numpy as np
from kiloncore import context, adb, consts
from cnocr import CnOcr

# 获取屏幕分辨率
def getWandH(ctx: context.Context):
    adb.screencap(ctx)
    src = cv2.imread(consts.screencap, cv2.IMREAD_GRAYSCALE)
    sw, sh = src.shape[::-1]
    return sw, sh

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


# 读取图片数字
def digitalRecognition(image):
    ocr = CnOcr(det_model_fp='resource/cnorcmodel/en_PP-OCRv3_det_infer.onnx') 
    result = ocr.ocr(image)
    res = ''.join([i for i in result[0]['text'] if i.isdigit()])
    return int(res)

# 裁剪截图模板区域
def imageTailor(ctx: context.Context,template_path):
    # 截图
    adb.screencap(ctx)
    # 读取模板和图像
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.imread(consts.screencap, cv2.IMREAD_GRAYSCALE)

    # 模板匹配
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    # 找到最佳匹配位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val < 0.6:
        return False, None

    top_left = max_loc

    # 计算剪裁的右下角位置
    bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])

    # 剪裁图像
    cropped_image = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]

    return True, cropped_image

# 读取剩余活性
def residualActivity(ctx: context.Context):
    flag, image = imageTailor(ctx, consts.cellActive)
    if not flag:
        return flag, None
    return True, digitalRecognition(image)

# 读取深度解析次数
def residualAnalysis(ctx: context.Context):
    flag, image = imageTailor(ctx, consts.depthanalysis)
    if not flag:
        return flag, None
    return True, digitalRecognition(image)

# 读取需要多少活性
def howMachActive(ctx: context.Context):
    flag, image = imageTailor(ctx, consts.recurrence)
    if not flag:
        return flag, None
    return True, digitalRecognition(image)