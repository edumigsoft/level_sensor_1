#
#
#
import const
import connect
import network
import json

try:
    import urequests as requests
except:
    import requests
try:
    import usocket as _socket
except:
    import _socket
try:
    import ussl as ssl
except:
    import ssl
#
#
#
update_id = "423322086"


def getMessage(messages):
    
    global update_id
    
    if (connect.do_connect()):

        s = _socket.socket()
    
        ai = _socket.getaddrinfo(const.TELEGRAM_API, const.TELEGRAM_PORT)
        #print("Address infos:", ai)
        addr = ai[0][-1]

        print("Connect address:", addr)
        print("Telegram")
        s.connect(addr)
    
        s.settimeout(const.TELEGRAM_TIMEOUT)
    
        s = ssl.wrap_socket(s)
        #print(s)
        print("\r\n")

        getRequest = "GET /bot"
        getRequest += const.TELEGRAM_TOKEN
        getRequest += messages
        getRequest += " HTTP/1.0\r\n\r\n"

        s.write(getRequest)
        quote = s.read(4096)
        #print(quote)
        #quote = quote.decode("ascii")
        #print(quote)
        #print("\r\n")
        #if (len(quote) > 0):
        #    #print(quote)
        #    quote = quote[379:]
        #    retJson = json.loads(quote)
        #    print(retJson["result"])
        #    #print(retJson["result"][0]["update_id"])
        #    temp = retJson["result"][0]["update_id"]
        #    up_id = int(str(temp))
        #    print("up_id = " + str(up_id))
        #    up_id2 = int(str(update_id))
        #    print("up_id2 = " + str(up_id2))
        #    if (up_id >= up_id2):
        #        update_id = str(retJson["result"][0]["update_id"] + 1)
        #        print("Json update_id + 1 = " + update_id)
        #else:
        #    print("Not message >> Last update_id = " + update_id)

        #print("\r\n")
        s.close()
        return quote

    
def getUpdates():
    
    up_id = int(str(update_id))
    updates = "/getUpdates";
    updates += "?";
    updates += "&limit=" + str(1);
    #updates += "&timeout=" + str(100);
    updates += "&offset=" + up_id + 1;
    #updates += "&offset=" + up_id;
    
    messages = getMessages(updates)
    print("getUpdates")
    print(messages)
    print("\r\n")


def getMe():
    
    updates = "/getMe";
    
    messages = getMessages(updates)
    print("getMe")
    print(messages)
    print("\r\n")
    
