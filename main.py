import requests
TOKEN = '2619421814940190'
url_hero = f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos'

req = requests.get(url_hero).json()
results = req['results']

for item in results:
    # print(item)
    for keys, values in item.items():
        # print(keys, values)
        if keys == 'powerstats':
            print(values['intelligence'])
            break