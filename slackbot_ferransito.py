import time
from slackclient import SlackClient

token = "XXXX-TOKEN-XXXXX"
sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        print sc.rtm_read()
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"
