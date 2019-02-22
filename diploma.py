import requests
from pprint import pprint
import time

user_name = 'eshmargunov'
ID = 171691064

with open('take_token.txt', encoding='utf-8') as f:
    TOKEN = f.read()

# TOKEN = input('Введите TOKEN')

params = {
    'v': '5.92',
    'access_token': TOKEN,
    'user_id': ID,
    # 'screen_name': user_name
}


def get_groups():  # группы пользователя
    params['extended'] = 1
    params['fields'] = 'members_count'
    resp_js_gr = requests.get('https://api.vk.com/method/groups.get', params).json()
    # for group in resp_js_gr:
    #     print(group["name"])
    return resp_js_gr['response']['items']


def get_friends():  # друзья пользователя
    resp_js = requests.get('https://api.vk.com/method/friends.get', params).json()
    return resp_js['response']['items']


def friends_groups():  # группы друзей
    c = 0
    friends_grouplist = []
    for friends in get_friends():
        c += 1
        print('-', c)
        params['user_id'] = friends['id']
        response = requests.get('https://api.vk.com/method/groups.get', params)
        print(response.json())
        try:
            resp_js = response.json()['response']['items']
            print(resp_js)
            friends_grouplist.append(resp_js)
        except KeyError:
            if response.json()['error']['error_code'] == 6:
                time.sleep(0.6)
            print('Ошибка 7. Нет прав для выполнения этого действия.')
    return friends_grouplist


def answer_for_d():
    user_groups = get_groups()
    # pprint(user_groups)
    user_friends_groups = friends_groups()
    # pprint(user_friends_groups)
    i = 0
    while i < len(user_groups):
        for group in user_friends_groups:
            if user_groups[i] in group:
                break
        else:
            with open('groups.json', 'a', encoding='utf-8') as fa:
                fa.write(str(user_groups[i]) + '\n')
        i += 1


# pprint(get_groups())
# pprint(get_friends())
# pprint(friends_groups())
answer_for_d()