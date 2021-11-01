import urllib.request
import json
import os
import hashlib

url_json = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
url_wiki = 'https://en.wikipedia.org/wiki/'


class JsonWiki:

    def __init__(self, url_json1):
        self.json = urllib.request.urlopen(url_json1)
        self.data = json.loads(self.json.read().decode())
        self.country_iter = iter(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self is None:
            raise StopIteration
        country_names = next(self.country_iter)['name']['common']
        country_list = country_names.split(' ')
        country_url = '_'.join(country_list)
        url_wiki_country = url_wiki + country_url
        with open('country_list.txt', 'a', encoding='utf-8') as file:
            file.write(f"{country_names} - {url_wiki_country}\n")
        return f'{country_names} - добавлена'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.json.close()


path_country_list = os.path.join(os.getcwd(), 'country_list.txt')


def my_generator(path_file):
    with open(path_file, mode='r', encoding='utf-8') as open_file:
        for line in open_file:
            hash_object = hashlib.md5(line.encode())
            yield hash_object.hexdigest()


if __name__ == '__main__':
    with JsonWiki(url_json) as data:
        for iter_data in data:
            print(iter_data)
    for item in my_generator(path_country_list):
        print(item)
