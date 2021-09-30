# задача 1
import requests
TOKEN = '2619421814940190'

url_heroes = [
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America'
    ]



all_chars = {}
for chars in url_heroes:
    req = requests.get(chars).json()
    results = req['results']
    for item in results:
        for keys, values in item.items():
            if keys == 'powerstats':
                all_chars[item['name']] = int(values['intelligence'])

# print(all_chars)

sorted_chars = dict(sorted(all_chars.items(), key=lambda x: x[1]))
print(f'Самый умный герой {max(sorted_chars)}, у него {max(sorted_chars.values())} интеллекта!')

# задача 2
from os import path
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}

        # получаем ссылки на все файлы
        all_links = []
        for file in file_path:
            url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
            r_get = requests.get(url, headers=headers, params={'path' : 'disk:/{}'.format(file), "overwrite": "true"})
            all_links.append(r_get.json()['href'])
            for links in all_links:
                r_put = requests.put(links, data=open('{}'.format(file), 'rb'))

if __name__ == '__main__':
    # В задании было получить от пользователя путь к загружаемому файлу и токен от пользователя.
    # я сделал вариант, когда все папки из конкретной директории заливаются в папку в облаке, буд-то сохранение фотографии на телефоне.

    current_dir = path.dirname(path.abspath(__file__))
    os.chdir(current_dir)
    os.chdir('files-to-upload')
    files_to_upload = os.listdir(os.getcwd())

    # токен не забыть удалить
    token = ''

    # иницилиазируем класс
    uploader = YaUploader(token)
    result = uploader.upload(files_to_upload)

# задача 3