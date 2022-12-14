import os
from PIL import Image
import tkinter.filedialog

filename = ""


def getPngPath():
    while True:     # 项目release xls_path
        filename = None
        try:
            print('*****请选择1024*1024大小的png文件')
            filename = tkinter.filedialog.askopenfilename()
        except:
            pass
        if filename is not None and filename != '':
            if os.path.isfile(filename):
                file_dxt = os.path.splitext(filename)[1]
                if file_dxt == ".png":
                    return filename
                else:
                    print('不支持其他文件，请选择png文件')
            else:
                print('您选择的是文件夹，请选择png文件')
        else:
            print('您没有选择任何文件')
            exit(0)


if __name__ == '__main__':
    piccc = [20, 29, 40, 58, 60, 76, 80, 87, 120, 152, 167, 180, 1024]

    filename = getPngPath()
    new_dir = os.path.dirname(filename) + '/'
    print('1024图片路径：%s' % filename)
    print('保存路径：%s' % new_dir)

    image = Image.open(filename)
    for cc in piccc:
        image_size = image.resize((cc, cc), Image.ANTIALIAS)
        image_size.save(new_dir + str(cc) + '.png')

