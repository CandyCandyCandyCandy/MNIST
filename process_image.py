import cv2
import os
global img

UPLOAD_PATH = os.getcwd()
def main(filename,ext):
    global img
    img = cv2.imread(filename)  # 手写数字图像所在位置
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转换图像为单通道(灰度图)
    resize_img = cv2.resize(img, (28, 28))  # 调整图像尺寸为28*28
    ret, thresh_img = cv2.threshold(resize_img, 127, 255, cv2.THRESH_BINARY)  # 二值化
    cv2.imwrite('processed_image.'+ext, thresh_img)  # 预处理后图像保存位置


