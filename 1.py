import cv2

img_root = 'C:/Users/Lenovo/Desktop/image/'  # 这里写你的文件夹路径，比如：/home/youname/data/img/,注意最后一个文件夹要有斜杠
fps = 5  # 保存视频的FPS，可以适当调整
size = (1920, 1080)
# 可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoWriter = cv2.VideoWriter('3.avi', fourcc, fps, size)  # 最后一个是保存图片的尺寸

# for(i=1;i<471;++i)
for i in range(1, 347):
    frame = cv2.imread(img_root + str(i) + '.jpg')
    videoWriter.write(frame)
videoWriter.release()

        # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
#         item = path + item
#         img = cv2.imread(item)
#         video.write(img)
#
# video.release()
# cv2.destroyAllWindows()