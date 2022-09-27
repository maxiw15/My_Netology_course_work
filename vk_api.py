import requests
import json
from my_token import TOKEN
from pprint import pprint


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

    def load_photo(self, data):
        photos = {}
        json_info = {}
        for elements in data["response"]["items"]:
            likes_count = str(elements["likes"]["count"])
            photo_url = elements["sizes"][-1]["url"]
            photo_size = str(elements["sizes"][-1]["height"]) + "*" + str(elements["sizes"][-1]["width"])
            if photo_url not in photos:
                photos[likes_count] = photo_url
                json_info[likes_count] = photo_size
            else:
                likes_count += "_id" + str(elements["id"])
                photos[likes_count] = photo_url
                json_info[likes_count] = photo_size
        json_file(json_info)
        return photos

    def get_photo(self, counter=5):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, "album_id": "profile", "photo_sizes": "1", "extended": "1", "count": counter}
        response = requests.get(url, params={**self.params, **params})
        return self.load_photo(response.json())


def json_file(json_info):
    with open('data.json', 'w') as outfile:
        json.dump(json_info, outfile)
