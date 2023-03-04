import time
from plyer import notification
import win32com.client as wc
t = input("Enter Remainder Title: ")
msg = input("Enter Remainder Message: ")
speaker = wc.Dispatch("SAPI.SpVoice")
count = 0
while True:
    notification.notify(
        title = t,
        message = msg,
        timeout= 20,
    )
    speaker.speak(msg) 
    time.sleep(20)
    if(count == 2):
        break
    count += 1
