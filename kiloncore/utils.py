from cv2 import (imread, matchTemplate, IMREAD_GRAYSCALE, TM_CCOEFF_NORMED, minMaxLoc, imwrite, INTER_LINEAR, 
                 resize, cvtColor, COLOR_BGR2GRAY, threshold, THRESH_BINARY_INV, findContours,CHAIN_APPROX_SIMPLE,
                 RETR_CCOMP, boundingRect, THRESH_BINARY)
from numpy import where
from kiloncore import context, adb, consts
# from cnocr import CnOcr

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
# def digitalRecognition(image):
#     try:
#         ocr = CnOcr(rec_vocab_fp="resource/cnorcmodel/label_cn.txt",
#                     rec_root="resource/cnorcmodel/",
#                     det_root="resource/cnorcmodel/") 
#         result = ocr.ocr(consts.temp)
        
#         res = ''.join([i for i in result[0]['text'] if i.isdigit()])

#         if res == "":
#             return 0
#         return int(res)
#     except Exception as ex:
#         print(ex)
#         return 0
def digitalRecognition(image, type):  
    # 加载数字模板
    temp_fp = "resource/template"
    template_paths = [f"{temp_fp}/{i}.png" for i in range(0,10)]
    templates = [imread(path, 0) for path in template_paths]
    
    img = imread(consts.temp)
    
    # 获取原始图像尺寸
    height, width = img.shape[:2]

    # 设置新的图像尺寸（放大两倍）
    new_width = 10 * width
    new_height = 10 * height

    # 放大图像
    resized_img = resize(img, (new_width, new_height), interpolation=INTER_LINEAR)

    gray = cvtColor(resized_img, COLOR_BGR2GRAY)

    # import cv2
    # cv2.imshow('1',gray)
    # cv2.waitKey(0)
    # 二值化
    if type == "white":
        _, binary = threshold(gray, 120, 255, THRESH_BINARY_INV)
    elif type == "black":
        _, binary = threshold(gray, 60, 255, THRESH_BINARY)
    elif type == "yellow":
        _, binary = threshold(gray, 100, 255, THRESH_BINARY_INV)
    # 查找轮廓
    contours, _ = findContours(binary, RETR_CCOMP,CHAIN_APPROX_SIMPLE)

    contour_info = []

    # 遍历每个轮廓，进行模板匹配
    for i, contour in enumerate(contours):
        # 获取轮廓的边界框
        x, y, w, h = boundingRect(contour)
        digit_img = binary[y:y+h, x:x+w]
        
        # 初始化最佳匹配分数和对应的数字
        best_score = 0
        best_match = -1

        # 遍历每个模板，进行匹配
        for i, template in enumerate(templates):
            # 调整轮廓图像的大小以匹配模板大小
            digit_img = resize(digit_img, templates[i].shape[::-1])

            # 使用相关性匹配方法
            
            result = matchTemplate(digit_img, template, TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = minMaxLoc(result)
            if max_val > best_score:
                best_score = max_val
                best_match = i

        # 将轮廓信息和识别的数字存储到列表中
        if best_score >0.7:
            contour_info.append((x, y, w, h, best_match))

    # 根据轮廓的x坐标对列表进行排序
    contour_info.sort(key=lambda x: x[0])

    # 计算
    res = 0
    for _, _, _, _, digit in contour_info:
        res = 10*res + digit
    return res


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

    imwrite(consts.temp, cropped_image)

    return True, cropped_image

# 读取剩余活性
def residualActivity(ctx: context.Context):
    flag, image = imageTailor(ctx, consts.cellActive)
    if not flag:
        return flag, None
    return True, digitalRecognition(image, "white")

# 读取深度解析次数
def residualAnalysis(ctx: context.Context):
    flag, image = imageTailor(ctx, consts.depthanalysis)
    if not flag:
        return flag, None
    return True, digitalRecognition(image, "yellow")

# 读取需要多少活性
def howMachActive(ctx: context.Context):
    flag, image = imageTailor(ctx, consts.recurrence)
    if not flag:
        return flag, None
    return True, digitalRecognition(image, "black")