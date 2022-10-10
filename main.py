from vk_api import VK
from yandex import YandexDisk
from progress.bar import Bar
import configparser  # импортируем библиотеку

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("my_token.ini")  # читаем конфиг


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

    access_token = config["VK"]["token"]

    user_id = input("id пользователя vk ")
    # user_id = "1"

    vk = VK(access_token, user_id)
    vk.get_albums()
    albums_list = vk.album_list
    temp = vk.temp_catalog
    print(temp)
    vk.json_file(temp)

    # TOKEN_Y = input("Введите токен с Полигона Яндекс диска ")
    ya = YandexDisk(token=config["YANDEX"]["token"])
    ya.create_folder("my_photos")
    upload_files(albums_list)
    print("Успешное завершение программы")
