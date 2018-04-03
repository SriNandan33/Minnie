from .import textToSpeech

from bs4 import BeautifulSoup
import requests


def quote_of_the_day():
    res = requests.get('https://www.brainyquote.com/quote_of_the_day')
    soup = BeautifulSoup(res.text, 'lxml')

    image_quote = soup.find('img', {'class': ' p-qotd bqPhotoDefault bqPhotoDefaultFw img-responsive'})
    
    quote = image_quote['alt']
    speech_output = quote.replace('-', 'by')
    print(quote)
    textToSpeech.speakout(speech_output)

if __name__ == '__main__':
    quote_of_the_day()