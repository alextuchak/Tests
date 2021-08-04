import requests

yad_token = 'AQAAAAAz3kTiAADLW4hKEMZnP0khv6FXKxCYVJ4'


class YadUpload:

    # Заголовки для запросов ЯндексДиска
    def get_yad_headers(self):
        return {'Contetn-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(yad_token)}

    # Создаем новую папку на ЯндексДиске и возвращаем путь к папке
    def put_back_up_folder(self, vk_id):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_yad_headers()
        params = {'path': vk_id}
        response = requests.put(url=url, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code == 201:
            print("Backup folder is created")
        return response.status_code

    def check_created_folder(self, vk_id):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_yad_headers()
        params = {'path': vk_id}
        response = requests.get(url, headers=headers, params={'path': vk_id})
        return response.status_code
