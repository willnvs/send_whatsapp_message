# https://pypi.org/project/pywhatkit/

import pywhatkit

### INSTRUCTIONS

#phone_num (required) - Phone number of target with country code
#message (required) - Message that you want to sendwhatmsg
#time_hour (required) - Hours at which you want to send message in 24 hour format
#time_min (required) - Minutes at which you want to send message
#wait_time (optional, val=20) - Seconds after which the message will be sent after opening the web
#print_waitTime (optional, val=True) - Will print the remaining time if set to true

pywhatkit.sendwhatmsg('+PHONE NUMBER', 'Message sent via Python', 18, 16)