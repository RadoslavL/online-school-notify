import datetime
import time
import os
looptimes = 0
player = "mpv"
beep = "beep.wav"
cmd = player+" "+beep
while True:
    looptimes += 1
    output = datetime.datetime.now()
    if output.hour == 13 and output.minute == 29 and output.second == 59:
        print("First class")
        os.system(cmd)
    elif output.hour == 14 and output.minute == 19 and output.second == 59:
        print("Second class")
        os.system(cmd)
    elif output.hour == 15 and output.minute == 9 and output.second == 59:
        print("Third class")
        os.system(cmd)
    elif output.hour == 16 and output.minute == 9 and output.second == 59:
        print("Forth class")
        os.system(cmd)
    elif output.hour == 16 and output.minute == 59 and output.second == 59:
        print("Fifth class")
        os.system(cmd)
    elif output.hour == 17 and output.minute == 49 and output.second == 59:
        print("Sixth class")
        os.system(cmd)
    elif output.hour == 18 and output.minute == 39 and output.second == 59:
        print("Seventh class")
        os.system(cmd)
        break
    elif output.hour == 18 and output.minute > 40 or output.hour > 18:
        break
    time.sleep(1)
    print("Loop", looptimes, "Completed")
print("Finished all seven classes for today!")
