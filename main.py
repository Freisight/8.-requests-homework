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

print(all_chars)

sorted_chars = dict(sorted(all_chars.items(), key=lambda x: x[1]))
print(f'Самый умный герой {max(sorted_chars)}, у него {max(sorted_chars.values())} интеллекта!')

# задача 2

import requests
token = 'AQAAAAAPbKQhAADLW0MqqyHBTUY2uNRimgs4mdI'

headers = {'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)}

# получение списка файлов и папок в текущей папке
# url = 'https://cloud-api.yandex.net:443/v1/disk/resources/'
# r = requests.get(url, headers=headers, params={'path' : 'disk:/Загрузки'})

# загрузка файлов на диск по URL
# url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
# r = requests.post(url, headers=headers, params={'path' : 'disk:/Загрузки', 'url' : 'https://yandex-images.clstorage.net/4TGM7i233/097191enaWKA/UAFOPv1Ke5ulnPNgy09YcLO-MbsczHwcyQTO0vdh3d3y0AM5piyeC7itj7HOidht4EVPPvNlw4Ln-jBndmgTsQDwn6v5Py9esT2EdUtOOZS2-0TOCG3Z6cglK7e2FTwYhxZmXacoWw4ta3-B_hgqn0J0qE1Bw-SFkA1EZzbIY9DhRJudH95qSWbOhZBL3gyxkr3jOf8LvVx7EIyzNEd9X4JxcSrHaotur6h5xGq9a35ihqnvEpBmV_D9RPcWOaATVzYZrB6raimGPpazCb6ew6P9g6sdWPyuSeN-wvZXjL-Cw6HJp3qon537CffrLio_EzaLTYKSB4dC7LXnV3ujMgTWmOzMahi7Zl7XoEodHlAz7FN6zkvefLtQrsA1p-yv85EDylVZSh2cuenG6kwpXFI1KH3zQIe2sH3ElnULcrNUN3jvrgvIOoX9tTFJz05BsK5R21zo_A7okkwAtBdejLNDMGlGuekPjDn6ZZu8K76h5jiuAiD0BUBPRSUWGJIiFsXq3HyryBtljxfQab6_8_I9sWovav996gDcc5c2LA9wgqHodLlKHp4aCoX4b_j8Qsb6PzKzpWUjrxVEt3kB80WXGvzfiyo5JAzEspssTRARz5DKHOseragyr6KHd57cgEEiGDVYOc59KQuU-y8LjtCHuRwxk_alwo0319SJgMAXRRhMvMtLWNae5wM4LN2zgR9yizwpzBx7Eq6wBpQObLCws7kFWNsOnZgqNHs-qR_AxboOYxCnR4Ks13a3WzCBhDeqfgz4qhoWjGUzCqwes4GcI5jPGk98WJKfITZGLE-yETHLNJk5Xj6ZmBZLT8mP4wR4X9IQBPWgPPUnl3sykOVXOPx--Ojq9Y5GoGpNHjAiL0DITRrcLbjQTFJHpmwdUbMCWyarCy_9Kfq2Gm567DNEStwiUFbFEiw3hFZpIfGVd9odnNgIiLeP9QD4XF_iYC3hGdw6Pf46sVzDM'})

# print(r.status_code)


url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
r = requests.get(url, headers=headers, params={'path' : 'disk:/Загрузки/1.txt', "overwrite": "true"})
link = r.json()
# print(link)

link_end = link['href']
# print(r.text)
url_upload = link_end
r = requests.put(url_upload, data=open('1.txt', 'rb'))
print(r.status_code)



# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token

#     def upload(self, file_path: str):
#         """Метод загружает файлы по списку file_list на яндекс диск"""
#         # Тут ваша логика
#         # Функция может ничего не возвращать


# if __name__ == '__main__':
#     # Получить путь к загружаемому файлу и токен от пользователя
#     path_to_file = ...
#     token = ...
#     uploader = YaUploader(token)
#     result = uploader.upload(path_to_file)

    

    