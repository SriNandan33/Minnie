from .import textToSpeech
import requests
from bs4 import BeautifulSoup


def read_news():
    response = requests.get('https://timesofindia.indiatimes.com/news')
    bs = BeautifulSoup(response.text, 'html.parser')

    main_div = bs.find("div", {'class': 'listing4'})
    lis = main_div.find_all("li", {"class": "clearfix"})

    for li in lis:
        news_title = li.find("strong").find("a").get("title")
        print(news_title, end="\n\n")
        textToSpeech.speakout(news_title)
