import cv2
import numpy as np
from PIL import Image

# 计算每个方块的大小像素
def get_cell_size(img: Image, x, y, x2, y2):
    for j in range(x, x2):
        for i in range(y, y2):
            pix = img.getpixel((j, i))
            if pix[:3] == (255, 255, 255):
                return j - x # 每个黑色格子的像素点大小


def get_cell(img: Image, w: int, h: int):
    flag = 0
    for y in range(h):
        for x in range(w):
            pix = img.getpixel((x, y))

            if pix[:3] == (0, 0, 0) and flag == 0: # 出现第一个黑色像素
                x1 = x
                flag = 1

            if pix[:3] == (255, 255, 255) and flag == 1: # 出现第一个白色像素（意味着左上角的标记方块横向结束）
                flag = 2
                cell = get_cell_size(img, x1, x1, x, x)
                return cell


unicode_chr = " ▗▖▄▝▐▞▟▘▚▌▙▀▜▛█"

def get_qrcode(cell, img: Image, w: int, h: int):
    height = int(h / cell)
    width = int(w / cell)
    bitcode = []
    for y in range(height):
        bitcode_row = []
        for x in range(width):
            pix = img.getpixel((x * cell, y * cell))
            if pix[:3] == (0, 0, 0):
                bitcode_row.append(1)
            if pix[:3] == (255, 255, 255):
                bitcode_row.append(0)
        bitcode.append(bitcode_row)

    if len(bitcode) % 2 == 1:
        bitcode_row = [0] * len(bitcode[0])
        bitcode.append(bitcode_row)

    bitarr = np.array(bitcode, dtype=np.uint8)

    H, W = bitarr.shape
    code = ""

    for i in range(1, H, 2):
        for j in range(1, W, 2):
            char_index = (
                (bitarr[i - 1, j - 1] << 3)
                + (bitarr[i - 1, j] << 2)
                + (bitarr[i, j - 1] << 1)
                + bitarr[i, j]
            )
            code += unicode_chr[char_index]
        code += "\n"

    print(code)


if __name__ == "__main__":
    im = cv2.imread("qrcode.png")
    im[im < 128] = 0
    im[im >= 128] = 255
    height, width = im.shape[:2]
    pil_image = Image.fromarray(im)
    get_qrcode(get_cell(pil_image, width, height), pil_image, width, height)
