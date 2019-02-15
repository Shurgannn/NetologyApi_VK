from urllib.parse import urlencode
import requests
from pprint import pprint

APP_ID = 6862336
AUTH_URL = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status,friends',
    'response_type': 'token',
    'v': '5.92',
}

#print('?'.join((AUTH_URL, urlencode(auth_data))))

TOKEN = '9fe89e091c0ddea40f26dd811ba3160e16b7241e31c4f9e30446299c4d339e5a3455111220dbedfed9774'

#params = {
#    'v': '5.92',
#    'access_token': TOKEN,
#    'text': '!'
#}
#response = requests.get('https://api.vk.com/method/status.set', params)
#pprint(response.json())


class User:

    def __init__(self, token):
        self.token = token

    def get_params(self):
        return {
            'v': '5.92',
            'access_token': TOKEN
        }

   # def friends_id(self):
    #    params = self.get_params()
     #   params['fields'] = 'o'
      #  response = requests.get('https://api.vk.com/method/friends.get', params)
       # pprint(response.json())
        #return response.json()

    def friends(self):
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/users.get', params)
        pprint(response.json())
        return response.json()



    def get_friends(self, uid):
        params = self.get_params()
        params['target_uid'] = uid
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        pprint(response.json())
        return response.json()



user = User(TOKEN)
#user.get_status()
#user.set_status('?')
#user.get_status()
user.get_friends(45567)
user.friends()