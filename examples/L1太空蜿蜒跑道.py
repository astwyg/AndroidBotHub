import os, json
import cv2

video_src = '..\\bots\\L1太空蜿蜒跑道.mp4'
tmp_path = '..\\tmp'

def split_video():
    cap = cv2.VideoCapture(video_src)
    frame_count = 1
    success = True

    while(success):
        success, frame = cap.read()
        if success == True and frame_count%10==0:
            cv2.imwrite(tmp_path + "\\frame%d.jpg" % frame_count,frame)
        frame_count = frame_count + 1

def get_actions():
    '''
    这个方法要根据视频切片结果自己写, ps取色的x,y<rgb> 对应frame[y,x]<bgr>
    left: 258, 90 : R>180
    right: 169, 257 : R>180
    draft: 573, 259 : R>200
    small_no2: 467, 230 : G>200
    no2_1: 522, 202 : G>240
    no2_2: 575, 201 : G>240
    :return: 
    '''
    cap = cv2.VideoCapture(video_src)
    frame_count = 1
    success = True

    actions = {}
    while (success):
        success, frame = cap.read()
        if success == True :
            # cv2.imwrite(tmp_path + "\\frame%d.jpg" % frame_count, frame)
            action = []
            if frame[90, 258][2] > 180:
                action.append("left")
            if frame[257, 169][2] > 180:
                action.append("right")
            if frame[259, 573][2] > 200:
                action.append("draft")
            if frame[230, 467][1] > 240:
                action.append("small_no2")
            if frame[202, 522][1] > 240:
                action.append("no2_1")
            if frame[202, 575][1] > 240:
                action.append("no2_2")
            actions[frame_count] = action
        frame_count = frame_count + 1

    with open("..\\bots\\L1太空蜿蜒跑道.json", "r") as f:
        data = json.load(f)
        with open("..\\bots\\L1太空蜿蜒跑道-script.json", "w") as fw:
            data["script"] = actions
            json.dump(data, fw)

if __name__ == "__main__":
    # split_video()
    get_actions()