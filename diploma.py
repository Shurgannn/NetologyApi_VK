import requests
from pprint import pprint
import time

user_name = 'eshmargunov'
id = 171691064
TOKEN = 'ed1271af9e8883f7a7c2cefbfddfcbc61563029666c487b2f71a5227cce0d1b533c4af4c5b888633c06ae'

params = {
    'v': '5.92',
    'access_token': TOKEN,
    'user_id': id
}
def get_groups():
    #groupslist = []
    params['extended'] = 1
    resp_js_gr = requests.get('https://api.vk.com/method/groups.get', params).json()['response']['items']
    #pprint(resp_js)
    #groupslist.append(resp_js)
    #pprint(groupslist)
    #return groupslist
    return resp_js_gr

def get_friends():
    resp_js = requests.get('https://api.vk.com/method/friends.get', params).json()['response']['items']
    #pprint(resp_js)
    return resp_js

def friends_groups():
    c = 0
    friends_grouplist = []
    for friends in get_friends():
        c += 1
        print('-', c)
        params['user_id'] = friends
        response = requests.get('https://api.vk.com/method/groups.get', params)
        time.sleep(0.6)
        try:
            resp_js = response.json()['response']['items']
            friends_grouplist.append(resp_js)
            #print(resp_js)
        except KeyError:
            print('Ошибка 7. Нет прав для выполнения этого действия.')
    #pprint(friends_grouplist)
    return friends_grouplist

def answer_for_d():
    answer_list = []
    user_groups = get_groups()
    user_friends_groups = friends_groups()
    i = 0
    while i < len(user_groups):
        for group in user_friends_groups:
            if user_groups[i] in group:
                    break
        else:
            answer_list.append(user_groups[i])
            #pprint(user_groups[i])
        i += 1
    pprint(answer_list)




#pprint(get_groups())
#print(get_groups())
#get_friends()
#friends_groups()
answer_for_d()