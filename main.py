import requests
from my_token import TOKEN

class VK:

   def __init__(self, access_token, user_id, version='5.131'):
       self.token = access_token
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/users.get'
       params = {'user_ids': self.id}
       response = requests.get(url, params={**self.params, **params})
       return response.json()


if __name__ == '__main__':
    access_token = TOKEN
    user_id = '260909074'
    vk = VK(access_token, user_id)
    print(vk.users_info())

