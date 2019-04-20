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
def Telegram_get():
    global update_id
    
    if (connect.do_connect()):

        s = _socket.socket()
    
        ai = _socket.getaddrinfo(const.TELEGRAM_API, const.TELEGRAM_PORT)
        print("Address infos:", ai)
        addr = ai[0][-1]

        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print("Connect address:", addr)
        print("Telegram")
        s.connect(addr)
    
        s.settimeout(3.0)
    
        s = ssl.wrap_socket(s)
        print(s)
        print("\r\n")

        getRequest = "GET /bot"
        getRequest += const.TELEGRAM_TOKEN
        getRequest += "/getUpdates"
        getRequest += "?"
        getRequest += "&limit=1"
        getRequest += "&timeout=100"
        getRequest += "&offset=" + update_id
        getRequest += " HTTP/1.0\r\n\r\n"
        #getRequest += 
        s.write(getRequest)
        quote = s.read(4096)
        quote = quote.decode("ascii")
        #print(quote)
        #print("\r\n")
        if (len(quote) > 0):
            #print(quote)
            quote = quote[379:]
            retJson = json.loads(quote)
            print(retJson["result"])
            #print(retJson["result"][0]["update_id"])
            temp = retJson["result"][0]["update_id"]
            up_id = int(str(temp))
            print("up_id = " + str(up_id))
            up_id2 = int(str(update_id))
            print("up_id2 = " + str(up_id2))
            if (up_id >= up_id2):
                update_id = str(retJson["result"][0]["update_id"] + 1)
                print("Json update_id + 1 = " + update_id)
        else:
            print("Not message >> Last update_id = " + update_id)

        print("\r\n")
        s.close()
#
#
#
def Firebase_get():
    #global update_id
    #update_id="423322083"
    
    if (connect.do_connect()):
        
        #s = _socket.socket()
    
        #ai = _socket.getaddrinfo(const.FIREBASE_HOST, const.FIREBASE_PORT)
        #print("Address infos:", ai)
        #addr = ai[0][-1]

        #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #print("Connect address:", addr)
        print("Firebase")
        URL = const.FIREBASE_HOST
        #URL += "/" + const.FIREBASE_LEDSTATUS
        #URL += "/" + const.FIREBASE_LAST_MESSAGE
        
        print(URL)
        if '.firebaseio.com' not in URL.lower():
            if '.json' == URL[-5:]:
                URL = URL[:-5]
            if '/' in URL:
                if '/' == URL[-1]:
                    URL = URL[:-1]
                URL = 'https://' + \
                      URL.split('/')[0] + '.firebaseio.com/' + URL.split('/', 1)[1] + '.json'
            else:
                URL = 'https://' + URL + '.firebaseio.com/.json'
            return URL

        if 'http://' in URL:
            URL = URL.replace('http://', 'https://')
        if 'https://' not in URL:
            URL = 'https://' + URL
        if '.json' not in URL.lower():
            if '/' != URL[-1]:
                URL = URL + '/.json'
            else:
                URL = URL + '.json'
        
        response = requests.get(URL)
        print(response.status_code)
        print(response.text)
# 200
# {"LEDStatus":0,"RFID-DEC":"74176183122","RFID-HEX":"3A424D43","last_message":423322063,"tank1":85,"tank2":60}
        
        
        #s.connect(addr)
    
        #s.settimeout(3.0)
    
        #s = ssl.wrap_socket(s)
        #print(s)
        #print("\r\n")



        
# Get
#curl 'https://samplechat.firebaseio-demo.com/users/jack/name.json'


# Node expecifico
#curl -X PATCH -d '{"last":"Jones"}' 'https://samplechat.firebaseio-demo.com/users/jack/name/.json'



#        getRequest = "GET /bot"
#        getRequest += const.tokenTelegram
#        getRequest += "/getUpdates"
#        getRequest += "?"
#        getRequest += "&limit=1"
#        getRequest += "&timeout=100"
#        getRequest += "&offset=" + update_id
#        getRequest += " HTTP/1.0\r\n\r\n"
#        #getRequest += 
#        s.write(getRequest)
#        quote = s.read(4096)
#        quote = quote.decode("ascii")
        #print(quote)
#        #print("\r\n")
#        if (len(quote) > 0):
#            #print(quote)
#            quote = quote[379:]
#            retJson = json.loads(quote)
#            print(retJson["result"])
#            #print(retJson["result"][0]["update_id"])
#            temp = retJson["result"][0]["update_id"]
#            up_id = int(str(temp))
#            print("up_id = " + str(up_id))
#            up_id2 = int(str(update_id))
#            print("up_id2 = " + str(up_id2))
#            if (up_id >= up_id2):
#                update_id = str(retJson["result"][0]["update_id"] + 1)
#                print("Json update_id + 1 = " + update_id)
#        else:
#            print("Not message >> Last update_id = " + update_id)
#
#        print("\r\n")
        #s.close()
