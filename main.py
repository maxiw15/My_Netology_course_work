from vk_api import VK
from yandex import YandexDisk
from my_token import TOKEN_VK, TOKEN_Y
from progress.bar import Bar


def upload_files(album_list):
    for album in album_list:
        bar = Bar(f'Загружаем файлы на Яндекс Диск из альбома {album}', max=5)
        dict_with_photo = vk.get_photo(album)
        for name, link in dict_with_photo.items():
            name = "my_photos/" + name
            ya.upload_file_to_disk(name, link)
            bar.next()
        bar.finish()


if __name__ == '__main__':
    print("Здравствуйте, введите пожалуйста следующие данные:")
    file = open("data.json", "w")
    file.close()

    access_token = TOKEN_VK
    user_id = input("id пользователя vk ")
    # user_id = "1"

    vk = VK(access_token, user_id)
    vk.get_albums()
    albums_list = vk.album_list

    TOKEN_Y = input("Введите токен с Полигона Яндекс диска ")
    ya = YandexDisk(token=TOKEN_Y)
    ya.create_folder("my_photos")
    upload_files(albums_list)
    print("Успешное завершение программы")
