import bs4
import requests


def find_posts(data: str, words: list, headers):
    url = 'https://habr.com'
    soup = bs4.BeautifulSoup(data, features="html.parser")
    articles = soup.find_all(class_="tm-articles-list__item")
    for article in articles:
        href = article.find(class_="tm-article-snippet__title-link").attrs['href']
        article_url = url + href
        article_response = requests.get(article_url, headers=headers).text
        article_soup = bs4.BeautifulSoup(article_response, features="html.parser")
        article_text = article_soup.find(class_="article-formatted-body").text
        for word in words:
            if word in article_text:
                article_title = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').text
                article_time = article.find('time').attrs["title"]

                print(f'{article_title} __ {article_time} __ {article_url}')
                break
