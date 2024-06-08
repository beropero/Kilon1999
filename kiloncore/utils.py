from cv2 import imread, matchTemplate, IMREAD_GRAYSCALE, TM_CCOEFF_NORMED, minMaxLoc
from numpy import where
from kiloncore import context, adb, consts
from cnocr import CnOcr

# 获取屏幕分辨率
def getWandH(ctx: context.Context):
    adb.screencap(ctx)
    src = imread(consts.screencap, IMREAD_GRAYSCALE)
    sw, sh = src.shape[::-1]
    return sw, sh

# 图片模板寻址
def whereTemplate(ctx: context.Context,template_path):
    adb.screencap(ctx)

    src = imread(consts.screencap, IMREAD_GRAYSCALE)

    # 加载模板图像
    template = imread(template_path, IMREAD_GRAYSCALE)

    # 确保模板图像小于源图像
    if src.shape[:2] < template.shape[:2]:
        print("模板图像应小于源图像")
        exit(1)

    # 计算模板的宽度和高度
    w, h = template.shape[::-1]
    sw, sh = src.shape[::-1]
    # 进行模板匹配
    res = matchTemplate(src, template, TM_CCOEFF_NORMED)
    
    # 设置阈值
    threshold = 0.8
    
    # 找到匹配的位置
    loc = where(res >= threshold)
    if len(loc[0]) == 0 or len(loc[1]) == 0:
        return -1, -1
    x = loc[1][0] + 1/2 * w
    y = loc[0][0] + 1/2 * h

    return sh - y, x


# 读取图片数字
def digitalRecognition(image):
    ocr = CnOcr(det_model_fp='resource/cnorcmodel/en_PP-OCRv3_det_infer.onnx',
                rec_vocab_fp="resource/cnorcmodel/label_cn.txt",
                rec_model_fp="resource/cnorcmodel/cnocr-v2.3-densenet_lite_136-gru-epoch=004-ft-model.onnx") 
    result = ocr.ocr(image)
    res = ''.join([i for i in result[0]['text'] if i.isdigit()])
    if res == "":
        return 0
    return int(res)

# 裁剪截图模板区域
def imageTailor(ctx: context.Context,template_path):
    # 截图
    adb.screencap(ctx)
    # 读取模板和图像
    template = imread(template_path, IMREAD_GRAYSCALE)
    image = imread(consts.screencap, IMREAD_GRAYSCALE)

    # 模板匹配
    result = matchTemplate(image, template, TM_CCOEFF_NORMED)

    # 找到最佳匹配位置
    min_val, max_val, min_loc, max_loc = minMaxLoc(result)

    if max_val < 0.3:
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