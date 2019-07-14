import os
import cv2

video_src = '..\\bots\\L1下坡漂移.mp4'
tmp_path = '..\\tmp'

def analysis_video():
    cap = cv2.VideoCapture(video_src)
    frame_count = 1
    success = True

    while(success):
        success, frame = cap.read()
        if success == True and frame_count%10==0:
            cv2.imwrite(tmp_path + "\\frame%d.jpg" % frame_count,frame)
        frame_count = frame_count + 1

if __name__ == "__main__":
    analysis_video()