import requests
import json
from progress.bar import Bar


class VK:

    def __init__(self, access_token, user_id, version='5.131'):
        self.album_list = ["wall", "profile"]
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def search_in_albums(self):
        for album in self.album_list:
            return self.get_photo(album_name=album)

    def load_photo(self, data):
        bar = Bar('Скачиваем фотографии из Вконтакте', max=5)
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
            bar.next()
        bar.finish()
        json_file(json_info)
        return photos

    def get_photo(self, album_name, counter=5):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, "album_id": album_name, "photo_sizes": "1", "extended": "1", "count": counter}
        response = requests.get(url, params={**self.params, **params})
        return self.load_photo(response.json())

    def get_albums(self):
        url = 'https://api.vk.com/method/photos.getAlbums'
        params = {'owner_id': self.id}
        response = requests.get(url, params={**self.params, **params})
        for album in response.json()["response"]["items"]:
            return self.album_list.append(str(album["id"]))


def json_file(json_info):
    with open('data.json', 'a') as outfile:
        json.dump(json_info, outfile)
        outfile.write("\n")
