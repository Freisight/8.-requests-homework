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

