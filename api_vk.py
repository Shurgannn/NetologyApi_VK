from urllib.parse import urlencode
import requests
from pprint import pprint

# APP_ID = 6862336
# AUTH_URL = 'https://oauth.vk.com/authorize'
# auth_data = {
#    'client_id': APP_ID,
#    'display': 'page',
#    'scope': 'status,friends',
#    'response_type': 'token',
#    'v': '5.92',
# }

TOKEN = input('Введите TOKEN')

class User:

    def get_params(self):
        return {
            'v': '5.92',
            'access_token': TOKEN,
        }

    def __init__(self, ID):
        self.ID = ID

    def __and__(self, other):
        params = self.get_params()
        params['source_uid'] = self.ID
        params['target_uid'] = other.ID
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        pprint(response.json()['response'])

    def __str__(self):
        vk_link = 'https://vk.com/id'
        return (f'{vk_link}{self.ID}')

    #def get_friends(self, uid):
    #    params = self.get_params()
    #    params['source_uid'] = self.ID
    #    params['target_uid'] = uid
    #    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    #    pprint(response.json())
    #    return response.json()



user1 = User(809170)
user2 = User(78865010)
#user1.get_status()
#user.set_status('?')
#user.get_status()
#user1.get_friends(user2.ID)
user1&user2
print(user2)