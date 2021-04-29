'''
Opencv-python读取IP摄像头视频流/USB摄像头
'''
import time

import cv2
from pyzbar import pyzbar


def rtsp():
    global cap, ret, frame
    # url = 'rtsp://admin:Admin@192.168.9.201:554/11'
    url = 'rtsp://admin:Admin123@192.168.9.201:554'
    cap = cv2.VideoCapture(url)
    count = 1
    print('IP摄像头是否开启： {}'.format(cap.isOpened()))
    # 显示缓存数
    print(cap.get(cv2.CAP_PROP_BUFFERSIZE))
    ret, frame = cap.read()
    # cv2.imshow('frame', frame)
    i = 0
    time_fps = 12
    j = 0
    while ret:
        i = i + 1
        if i % time_fps == 0:
            j = j + 1
            cv2.imwrite(f'test_{count}.jpg', frame)
            print(f'save count {count}')
            count = count + 1
            if count>10:
                break
        success, frame = cap.read()
    # time.sleep(5)



    # while (cap.isOpened()):
    #     ret, frame = cap.read()
    #     cv2.imshow('frame', frame)
    #     cv2.imwrite(f'test_{count}.jpg', frame)
    #     # time.sleep(5)
    #     count = count+1
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    cap.release()
    cv2.destroyAllWindows()


def http():
    global cap, ret, frame
    # 创建一个窗口 名字叫做Window
    cv2.namedWindow('Window', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
    '''
        #打开USB摄像头
        cap = cv2.VideoCapture(0)
        '''
    # 摄像头的IP地址,http://用户名：密码@IP地址：端口/
    ip_camera_url = 'http://admin:Admin123@192.168.9.200:80/'
    # 创建一个VideoCapture
    cap = cv2.VideoCapture(ip_camera_url)
    print('IP摄像头是否开启： {}'.format(cap.isOpened()))
    # 显示缓存数
    print(cap.get(cv2.CAP_PROP_BUFFERSIZE))
    # 设置缓存区的大小
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    # 调节摄像头分辨率
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 设置FPS
    print('setfps', cap.set(cv2.CAP_PROP_FPS, 25))
    print(cap.get(cv2.CAP_PROP_FPS))
    while (True):
        # 逐帧捕获
        ret, frame = cap.read()  # 第一个参数返回一个布尔值（True/False），代表有没有读取到图片；第二个参数表示截取到一帧的图片
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Window', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 当一切结束后，释放VideoCapture对象
    cap.release()
    cv2.destroyAllWindows()





def decode_display(image):
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        # 提取二维码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # 提取二维码数据为字节对象，所以如果我们想在输出图像上
        # 画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (0, 0, 125), 2)

        # 向终端打印条形码数据和条形码类型
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    return image


def detect():
    url = 'rtsp://admin:Admin123@192.168.9.201:554'
    camera = cv2.VideoCapture(url)

    while True:
        # 读取当前帧
        ret, frame = camera.read()
        # 转为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        im = decode_display(gray)

        cv2.waitKey(5)
        cv2.imshow("camera", im)

    camera.release()


if __name__ == "__main__":
    # http()
    # rtsp()
    detect()