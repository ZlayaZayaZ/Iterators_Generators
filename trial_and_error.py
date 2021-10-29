import urllib.request
import json
import os
import hashlib

url_json = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
url_wiki = 'https://en.wikipedia.org/wiki/'
with urllib.request.urlopen(url_json) as url:
    data = json.loads(url.read().decode())
    for iter_data in data:
        country = iter_data['name']['common']
        country_list = country.split(' ')
        country_url = '_'.join(country_list)
        url_wiki_country = url_wiki + country_url
        with open('country_list.txt', 'a', encoding='utf-8') as file:
            file.write(f"{iter_data['name']['common']} - {url_wiki_country}\n")


path_country_list = os.path.join(os.getcwd(), 'country_list.txt')


def my_generator(path_file):
    with open(path_file, mode='r', encoding='utf-8') as open_file:
        for line in open_file:
            hash_object = hashlib.md5(line.encode())
            yield hash_object.hexdigest()


if __name__ == '__main__':
    for item in my_generator(path_country_list):
        print(item)


