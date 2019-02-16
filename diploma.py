import requests
from pprint import pprint

user_name = 'eshmargunov'
id = 171691064
TOKEN = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'

params = {
    'v': '5.92',
    'access_token': TOKEN,
    'user_id': id
}
def get_groups():
    params['extended'] = 1
    params['user_id'] = id
    response = requests.get('https://api.vk.com/method/groups.get', params)
    resp_js = response.json()['response']['items']
    pprint(resp_js)
    return resp_js

def get_friends():
    response = requests.get('https://api.vk.com/method/friends.get', params)
    resp_js = response.json()['response']['items']
    pprint(resp_js)
    return resp_js

def friends_groups():
    for friends in get_friends():
        id = friends
        get_groups()
        pprint(friends)
    #return resp_js

get_groups()
#get_friends()
#friends_groups()