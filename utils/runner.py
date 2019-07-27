import json, os, time, subprocess

def sh(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def run(bot_name, ms=200):
    if not bot_name:
        bot_name="L1太空蜿蜒跑道-script.json"
    with open("..\\bots\\"+bot_name, "r") as f:
        data = json.load(f)
        script = data["script"]
        actions = data["actions"]
        for s in range(1,len(script)):
            currnt_script = script[str(s)]
            print("{}:{}".format(s,script[str(s)]))
            if len(currnt_script):
                for cs in currnt_script:
                    cmd = "adb shell "+ actions[cs].format(ms=ms) + "\n"
                    sh(cmd)
            time.sleep(0.25)

if __name__=="__main__":
    os.system("adb devices")
    os.system("adb shell input swipe 354 865 355 866 1000")
    bot_name = input("bot name?\n")
    run(bot_name)