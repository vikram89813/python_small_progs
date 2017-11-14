import webbrowser
import time

total_break=3
count_ = 0;

while(count_ < total_break):
    print("current time : " + time.ctime())
    time.sleep(10)
    webbrowser.open("https://www.google.co.in/webhp?hl=en&ictx=2&sa=X&ved=0ahUKEwjN-uvN5L3XAhUBLY8KHfi6CBoQPQgD")
    count_=count_+1


