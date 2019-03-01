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
    resp_js_gr = requests.get('https://api.vk.com/method/groups.get', params).json()['response']['items']
    return resp_js_gr


def get_friends():  # друзья пользователя
    resp_js = requests.get('https://api.vk.com/method/friends.get', params).json()
    resp_j = resp_js['response']['items']
    return resp_j


def friends_groups():  # группы друзей
    i = 0
    set_user_groups = set(get_groups())
    friends = get_friends()
    while i < len(friends):
        print('-')
        params['user_id'] = friends[i]
        response = requests.get('https://api.vk.com/method/groups.get', params)
        try:
            set_friends_groups = set(response.json()['response']['items'])
            common_groups = (set_user_groups & set_friends_groups)
            set_user_groups = set_user_groups - common_groups
            i += 1
        except KeyError:
            if response.json()['error']['error_code'] == 6:
                print('Ошибка 6. Слишком много запросов в секунду.')
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
    return set_user_groups


def answer_for_d():
    i = 0
    unique_groups = list(friends_groups())
    list_answers_for_d = []
    while i < len(unique_groups):
        params['group_id'] = unique_groups[i]
        params['fields'] = 'members_count'
        response = requests.get('https://api.vk.com/method/groups.getById', params)
        try:
            resp_js_gr = response.json()['response']
            for g in resp_js_gr:
                d = {'name': g['name'],
                     'id': g['id'],
                     'members_count': g['members_count']
                     }
                list_answers_for_d.append(d)
            i += 1
        except KeyError:
            if response.json()['error']['error_code'] == 6:
                print('Ошибка 6. Слишком много запросов в секунду.')
                print(response.json())
                time.sleep(2)
    return list_answers_for_d


with open('groups.json', 'w', encoding='utf-8') as fw:
    json.dump(answer_for_d(), fw)

# print(get_groups())
# pprint(get_friends())
# pprint(friends_groups())
# answer_for_d()

# set_user_groups = set(get_groups())
# print(set_user_groups)
# pprint(get_friends())
# print(answer_for_d())