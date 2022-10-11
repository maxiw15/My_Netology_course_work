from vk_api import VK
from yandex import YandexDisk
from progress.bar import Bar
import configparser  # импортируем библиотеку
import json


def upload_files(album_list, count):
    for album in album_list:
        bar = Bar(f'Загружаем файлы на Яндекс Диск из альбома {album}', max=count)
        dict_with_photo = vk.get_photo(album, count)
        for name, link in dict_with_photo.items():
            name = "my_photos/" + name
            ya.upload_file_to_disk(name, link)
            bar.next()
        bar.finish()


if __name__ == '__main__':
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("my_token.ini")  # читаем конфиг
    print("Здравствуйте, введите пожалуйста следующие данные:")
    file = open("data.json", "w")
    file.close()
    access_token = config["VK"]["token"]
    vk = VK(access_token)
    print("Вы будете вводить id пользователя или его screen name?")
    answer = input("Для выбора введите 1 или 2 ")
    if answer == "1":
        user_id = input("id пользователя vk ")
    elif answer == "2":
        user_id = vk.get_id_with_screenname(screen_name=input("Введите screen name "))
    count = int(input("Введите количество фотографий, которые необходимо скачать "))
    vk = VK(access_token, bar_max=count, user_id=user_id)  # создаем объект ВК
    vk.get_albums()
    albums_list = vk.album_list
    TOKEN_Y = input("Введите токен с Полигона Яндекс диска ")
    # ya = YandexDisk(token=config["YANDEX"]["token"])
    ya = YandexDisk(token=TOKEN_Y)
    ya.create_folder("my_photos")
    upload_files(albums_list, count=vk.bar_max)

    with open('data.json', 'w') as outfile:  # запись в json файл
        json.dump(vk.temp_catalog, outfile)

    print("Успешное завершение программы")
