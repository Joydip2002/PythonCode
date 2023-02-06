#else Part Printing But Program Is okay
import smtplib

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("dastanumoy17@gmail.com","csbqrqjpgcpfwypb")

if(server.sendmail("dastanumoy17@gmail.com", "joydipmanna2002@gmail.com", "Hi, I am Tanumoy Das")):
    print("Mail Sending Successful")
else:
    print("Mail Sending Un-Successful")
 