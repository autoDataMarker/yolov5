import cv2
import sys
import os


def tracking(path1, path2, x1, y1, x2, y2):
    # 创建跟踪器
    tracker = cv2.MultiTracker_create()
    init_once = False
    # 读入视频
    video = cv2.VideoCapture(path1)
    # 读入第一帧
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    # 框选bounding box
    boxes = (int(x1), int(y1), int(x2) - int(x1), int(y2) - int(y1))
    cnt = 0
    while True:
        cnt += 1
        ok, frame = video.read()
        if not ok:
            break
        if not init_once:
            tracker.add(cv2.TrackerCSRT_create(), frame, (200,300,100,20))
            # region = frame[bbox[1]: bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]]
            init_once = True
        # 将列表转为元组
        # Update tracker
        # while 1:
        ok, box = tracker.update(frame)
        # Draw bonding box
        if ok:
            p1 = (int(box[0][0]), int(box[0][1]))
            p2 = (int(box[0][0] + box[0][2]), int(box[0][1] + box[0][3]))
            with open(str(path2) + 'new' + '.txt', 'a') as f:
                f.write(str(cnt))
                f.write(' ')
                f.write(str(p1[0]))
                f.write(' ')
                f.write(str(p1[1]))
                f.write(' ')
                f.write(str(p2[0]))
                f.write(' ')
                f.write(str(p2[1]))
                f.write('\n')
                cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

        # 展示tracker类型
        # cv2.putText(frame, tracker_type + "Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
        # 展示FPS
        # cv2.putText(frame, "FPS:" + str(fps), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
        # Result
        cv2.namedWindow('Tracking', 0)
        cv2.imshow("Tracking", frame)

        # Exit
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break
    video.release()
    cv2.destroyAllWindows()


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


if __name__ == '__main__':
    del_file(sys.argv[2])
    tracking(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
