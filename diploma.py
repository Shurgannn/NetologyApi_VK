import requests
from pprint import pprint
import time
import json

# user_name = input('Введите имя пользователя')# 'eshmargunov'
# ID = 171691064
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
    resp_j = resp_js['response']['items']
    # print(resp_j)
    return resp_j


def friends_groups():  # группы друзей
    i = 0
    friends_grouplist = []
    friends = get_friends()
    while i < len(friends):
        print('-')
        params['user_id'] = friends[i]['id']
        response = requests.get('https://api.vk.com/method/groups.get', params)
        try:
            resp_js = response.json()['response']['items']
            print(resp_js)
            friends_grouplist.append(resp_js)
            i += 1
        except KeyError:
            if response.json()['error']['error_code'] == 6:
                print('Ошибка 6.')
                print(response.json())
                time.sleep(2)
            elif response.json()['error']['error_code'] == 7:
                print('Ошибка 7. Нет прав для выполнения этого действия.')
                i += 1
                print(response.json())
            elif response.json()['error']['error_code'] == 18:
                print('Ошибка 18. Страница удалена или заблокирована.')
                print(response.json())
                i += 1
        print(i)
    return friends_grouplist


def answer_for_d():
    user_groups = get_groups()
    user_friends_groups = friends_groups()
    i = 0
    list_answers_for_d = []
    while i < len(user_groups):
        for group in user_friends_groups:
            if user_groups[i] in group:
                break
        else:
            pprint(user_groups[i])
            d = {
                'name': user_groups[i]['name'],
                'id': user_groups[i]['id'],
                'members_count': user_groups[i]['members_count']
            }
            list_answers_for_d.append(d)
        i += 1
    return list_answers_for_d


with open('groups.json', 'w', encoding='utf-8') as fw:
    json.dump(answer_for_d(), fw)

# print(get_groups())
# pprint(get_friends())
# pprint(friends_groups())
# answer_for_d()