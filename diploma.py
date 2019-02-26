import requests
from pprint import pprint
import time
import json

# user_name = input('Введите имя пользователя')# 'eshmargunov'
# ID = input('Введите id пользователя')# 171691064
users = input('Введите id или имя пользователя')

with open('take_token.txt', encoding='utf-8') as f:
    TOKEN = f.read()

# TOKEN = input('Введите TOKEN')

params = {
    'v': '5.92',
    'access_token': TOKEN,
    # 'user_id': ID,
    'user_ids': users,
}


def get_groups():  # группы пользователя
    params['extended'] = 1
    params['fields'] = 'members_count'
    resp_js_gr = requests.get('https://api.vk.com/method/groups.get', params).json()['response']['items']
    return resp_js_gr


def get_friends():  # друзья пользователя
    resp_js = requests.get('https://api.vk.com/method/friends.get', params).json()
    return resp_js['response']['items']


def friends_groups():  # группы друзей
    c = 0
    c2 = 0
    friends_grouplist = []
    for friends in get_friends():
        c += 1
        print('-', c)
        while c2 < c:
            params['user_id'] = friends['id']
            response = requests.get('https://api.vk.com/method/groups.get', params)
            try:
                resp_js = response.json()['response']['items']
                print(resp_js)
                friends_grouplist.append(resp_js)
                c2 += 1
            except KeyError:
                if response.json()['error']['error_code'] == 6:
                    print('Ошибка 6.')
                    time.sleep(0.8)
                elif response.json()['error']['error_code'] == 7:
                    print('Ошибка 7. Нет прав для выполнения этого действия.')
                    c2 += 1
                elif response.json()['error']['error_code'] == 18:
                    print('Ошибка 18. Страница удалена или заблокирована.')
                    c2 += 1
        print(c2)
    return friends_grouplist


def answer_for_d():
    user_groups = get_groups()
    # pprint(user_groups)
    user_friends_groups = friends_groups()
    # pprint(user_friends_groups)
    i = 0
    list_answers_for_d = []
    while i < len(user_groups):
        for group in user_friends_groups:
            if user_groups[i] in group:
                break
        else:
            pprint(user_groups[i])
            list_answers_for_d.append((user_groups[i])['name'])
        i += 1
    #for group in list_answers_for_d:
    #    del group['screen_name']
     #   del group['is_closed']
     #   del group['photo_100']
     #   del group['photo_200']
     #   del group['photo_50']
     #   del group['type']
    return list_answers_for_d


with open('groups.json', 'w', encoding='utf-8') as fw:
    json.dump(answer_for_d(), fw)

# print(get_groups())
# pprint(get_friends())
# pprint(friends_groups())
# answer_for_d()