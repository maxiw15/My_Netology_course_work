from my_token import TOKEN_Y
import requests


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def create_folder(self, name_folder):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources?"
        headers = {"Authorization": TOKEN_Y}
        params = {"path": name_folder}
        requests.put(upload_url, headers=headers, params=params)

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Authorization": TOKEN_Y}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, upload_url):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        file_response = requests.get(upload_url)
        response = requests.put(href, file_response)
        response.raise_for_status()
        if response.status_code != 201:
            print("\nНеудачная загрузка файла")
