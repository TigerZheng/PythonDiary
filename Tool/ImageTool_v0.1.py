"""
    Author：Tiger Z
    Time  ：2020-4-20 10:58:07
    Log   ：
        v0.1：
            初版，提取图片的像素点数据

"""
from PIL import Image
import numpy as np


def main():
    # 打开图像并转化为数字矩阵
    image = Image.open('./BG2.png')

    """
        可设置图片缩放的质量如下：
        Image.NEAREST：最低质量
        Image.BILINEAR：双线性，
        Image.BICUBIC：三次样条插值
        Image.ANTIALIAS：最高质量）
        
        该参数可缺省，但是转换后的效果比较差
    """
    image = image.resize((1000, 1000), Image.BILINEAR)

    # 新建窗口显示已打开的图片
    image.show()
    # 图片另存为
    # image.save('./save.png')
    # 将数据转化为矩阵
    image_array = np.array(image)

   # 输出图片矩阵的维度
    print(image_array.shape)

if __name__ == "__main__":
    main()
    


