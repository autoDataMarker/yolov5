import cv2
import os


def del_file(path_data):
    for i in os.listdir(path_data):
        path_file = os.path.join(path_data, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            for f in os.listdir(path_file):
                path_file2 = os.path.join(path_file, f)
                if os.path.isfile(path_file2):
                    os.remove(path_file2)
    for i in os.listdir(path_data):  # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = os.path.join(path_data, i)  # 当前文件夹的下面的所有东西的绝对路径
        os.rmdir(file_data)


def video2img(video, images):
    if not os.path.exists(images):
        os.mkdir(images)
    del_file(images)  # 保存帧图片前先清空文件夹

    cap = cv2.VideoCapture(video)  # 视频位置
    c = 0
    while 1:
        success, frame = cap.read()
        if success:
            cv2.imwrite(images + str(c) + '.jpg', frame)
            size = frame.shape
            c = c + 1
        else:
            break
    with open(images + 'size.txt', 'a') as f:
        f.write(str(size[0]))
        f.write(' ')
        f.write(str(size[1]))
        f.write('\n')
    cap.release()


if __name__ == '__main__':
    import sys

    video2img(sys.argv[1], sys.argv[2])
