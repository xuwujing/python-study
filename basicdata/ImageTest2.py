# 图片算法

from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
from skimage import io
import skimage
import pylab
import numpy as np
import cv2

# 遮挡
def cover():
    impath = "../image/578e56d9f3d054696e80be67bcbbefa.jpg"
    img1 = Image.open(impath)
    img1 = np.asarray(img1) / 255.00
    img2 = Image.open(impath)
    draw = ImageDraw.Draw(img2)
    draw.rectangle((60, 90, 100, 120), fill=(0, 0, 0))
    img2 = np.asarray(img2) / 255.00
    plt.figure(1)
    plt.subplot(121)
    plt.imshow(img1)
    plt.title("Origin picture")
    plt.subplot(122)
    plt.imshow(img2)
    plt.title("Add obstacle")
    plt.savefig("obstacle_image.jpg")
    pylab.show()

# 噪声
# 注意事项：
# Peckle, Poisson, Localvar, and Gaussian noise 加上噪声后，值可能为负值，也可能超过255；
# 默认情况下，clip参数值为True，将会clip掉这些超过区间的点，如果clip设置为False，就要注意有可能包含一些超过区间的点。
# Skimage读取图像是RGB，而Opencv是BGR
# Skimage读取图像后是(height, width, channel)<br>
def noise():
    impath = "000001.jpg"
    image = io.imread(impath)
    img1 = image / 255.00
    img2 = skimage.util.random_noise(image, mode='gaussian', seed=None, clip=True)
    plt.figure(1)
    plt.subplot(121)
    plt.imshow(img1)
    plt.title("Origin picture")
    plt.subplot(122)
    plt.imshow(img2)
    plt.title("Add Gaussian noise")
    pylab.show()
    plt.savefig("noise_image.jpg")

    #增加高斯噪声
    #shimage.util.random_noise(image, mode='gaussian', seed=None, clip=True)




# 模糊
def dim():
    impath = "000001.jpg"
    kernel_size = (5, 5)
    sigma = 1.5
    img11 = cv2.imread(impath)
    # BGR -> RGB
    b, g, r = cv2.split(img11)
    img11 = cv2.merge([r, g, b])
    # BGR -> RGB
    # img2=img[: , : , : : -1]
    img1 = img11 / 255.00
    img2 = cv2.GaussianBlur(img1, kernel_size, sigma)
    # cv2.imwrite(blur_image, img2)
    plt.figure(1)
    plt.subplot(121)
    plt.imshow(img1)
    plt.title("Origin picture")
    plt.subplot(122)
    plt.imshow(img2)
    plt.title("Add Gaussian Blur")
    plt.savefig("blur_image.jpg")
    pylab.show()




if __name__ == '__main__':
    cover()
    noise()
    dim()
