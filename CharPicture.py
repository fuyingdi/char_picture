from PIL import Image, ImageEnhance

codeset = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''  # 生成字符画所需的字符集


def convert_to_charpic(image, scale=1):
    """
    :param image: Image.Image object
    :param scale: narrow scale
    :return: string
    """
    con_result = ''
    assert isinstance(image, Image.Image)
    image.thumbnail((image.size[0] // scale * 2, image.size[1] // scale))
    if image.mode == 'RGB':
        for y in range(0, image.size[1], 2):
            for x in range(0, image.size[0]):
                r, g, b = image.getpixel((x, y))
                # 计算灰度值
                gray = r * 0.229 + g * 0.587 + b * 0.114
                con_result = con_result + codeset[int(20 * gray // 256)]
            con_result = con_result + '\r\n'
    elif image.mode == 'RGBA':
        for y in range(0, image.size[1]):
            for x in range(0, image.size[0]):
                r, g, b, a = image.getpixel((x, y))
                gray = r * 0.229 + g * 0.587 + b * 0.114
                print(int(gray // 256))
                con_result = con_result + codeset[int(20 * gray // 256)]
            con_result = con_result + '\r\n'
    return con_result


def contrast_enhance(image, scale):
    contrast = ImageEnhance.Contrast(image)
    result = contrast.enhance(scale)
    # result.show()
    return result

if __name__ == '__main__':
    im = Image.open('image.jpg')
    im = contrast_enhance(im, 100)
    result = convert_to_charpic(im, 10)
    print(result)
