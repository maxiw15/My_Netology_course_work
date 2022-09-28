from vk_api import VK
from yandex import YandexDisk
from my_token import TOKEN_VK, TOKEN_Y


def upload_files():
    dict_with_photo = vk.get_photo()
    for name, link in dict_with_photo.items():
        name = "my_photos/" + name
        ya.upload_file_to_disk(name, link)


if __name__ == '__main__':
    access_token = TOKEN_VK
    user_id = '1'
    vk = VK(access_token, user_id)
    ya = YandexDisk(token=TOKEN_Y)
    upload_files()


