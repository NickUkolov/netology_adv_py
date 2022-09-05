import requests
from user_agent import generate_navigator
import functions


KEYWORDS = ['дизайн', 'фото', 'web', 'python']


if __name__ == '__main__':
    a = int(input('Сколько страниц для поиска?'))
    base_url = 'https://habr.com'
    for number in range(1, a):
        url = base_url + f"/ru/all/page{number}"

        HEADERS = generate_navigator()

        response = requests.get(url, headers=HEADERS)
        text = response.text

        functions.find_posts(text, KEYWORDS, headers=HEADERS)
