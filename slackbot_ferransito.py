import time
from slackclient import SlackClient

token = "xoxb-14434545828-lJTOdN7fEUWFj5kShiqjm46C"
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        print sc.rtm_read()
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"


#general C0CTKKUAX