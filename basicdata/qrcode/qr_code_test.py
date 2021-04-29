import os
import webbrowser
from PIL import Image
from pyzbar import pyzbar


def decode_qr_code(code_img_path):
    if not os.path.exists(code_img_path):
        raise FileExistsError(code_img_path)
    return pyzbar.decode(Image.open(code_img_path), symbols=[pyzbar.ZBarSymbol.QRCODE])


if __name__ == "__main__":
    src = "/home/image/test.jpg"
    # src = "/home/image/Lark20210428-165847.jpeg"
    results = decode_qr_code(src)
    print(results[0].data.decode("utf-8"))