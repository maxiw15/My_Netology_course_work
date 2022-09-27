from vk_api import *


if __name__ == '__main__':
    access_token = TOKEN
    user_id = '1'
    vk = VK(access_token, user_id)
    pprint(vk.get_photo())
