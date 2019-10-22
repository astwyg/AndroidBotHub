import time, os
from utils.runner import sh

btn_go_to_shop = [883,1152]
swipe_start = [523, 2014]
swipe_end = [523, 210]


def run():
    sh("adb shell input tap {} {} \n".format(btn_go_to_shop[0], btn_go_to_shop[1]))
    time.sleep(5)
    for _ in range(10):
        sh("adb shell input swipe {} {} {} {} 800 \n".format(swipe_start[0], swipe_start[1], swipe_end[0], swipe_end[1]))
        time.sleep(2)
    sh("adb shell input keyevent 4 \n")
    time.sleep(1)

if __name__ == "__main__":
    os.system("adb devices")
    for _ in range(20):
        run()