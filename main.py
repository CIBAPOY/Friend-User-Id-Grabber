import requests
import json
import os

userid = input('Player Id: ')

friends = []

dir = os.path.dirname(os.path.abspath(__file__))
cook = os.path.join(dir, "cookie.txt")

f = open(cook, "r")
cookie = f.read()
f.close()

testing = requests.post('https://auth.roblox.com/v2/logout', cookies = {'.ROBLOSECURITY':cookie})

token = testing.headers['x-csrf-token']

header = {
    'cookie': cookie,
    'x-csrf-token': token
}

r = requests.get(f"https://friends.roblox.com/v1/users/{userid}/friends", headers=header)
response = str(r.content)
response = response[2:len(response)-1]

val = json.loads(response)
for i in range(0,len(val['data'])):
    friend = val['data'][i]['id']
    friends.append(friend)
print(friends)
input("\nFinished! (Press 'enter' to exit)")
