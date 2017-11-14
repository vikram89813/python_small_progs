import time
import webbrowser

total_ = 3
curr=0

while(curr < total_):
    print("curr time is : " + time.ctime() + "take break!!")
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=wJnBTPUQS5A")
    curr = curr + 1