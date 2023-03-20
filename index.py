import httpx
import json
import time
with open("message.txt", "r") as b:
    msg = b.read()
with open("channels.txt", "r") as s:
    ch = s.readlines()
config = json.load(open("config.json", "r+"))
TOKEN = config['token']

def send_message(message, channel_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    json = {
        "content": message,
        "tts": False
    }
    r = httpx.post(url, json=json, headers={"Authorization":TOKEN})
    return r
while True:
    for x in ch:
        x = x.split()[0]
        print(x)
        o = send_message(msg, x)    
        if o.status_code == 200:
            print(f"Sent in {x}")                
    time.sleep(config['interval']*3600)