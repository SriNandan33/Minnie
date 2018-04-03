from . import textToSpeech

from weather import Weather, Unit


def get_weather(json_response):
    weather = Weather(unit=Unit.CELSIUS)

    place = (json_response['result']['parameters']['place'])
    if not place:
        place = 'nuzvid'

    location = weather.lookup_by_location(place)
    forecasts = location.forecast()
    day = 0
    for forecast in forecasts:
        if day == 0:
            print('weather at {0}'.format(place))
            print('Weather Report: {0}'.format(forecast.text()))
            print('Maximum Temperature: {0}ºC'.format(forecast.high()))
            print('Minimum Temperature: {0}ºC'.format(forecast.low()))

            textToSpeech.speakout('weather report of {0}'.format(place))
            textToSpeech.speakout('{0}'.format(forecast.text()))
            textToSpeech.speakout('Maximum Temperature is {0} degree celsius'.format(forecast.high()))
            textToSpeech.speakout('Minimum Temperature is {0} degree celsius'.format(forecast.low()))
        day += 1
