import webbrowser


def get_directions(json_response):
    default_from_city = 'Nuzividu'  # todo: get current location
    from_city = (json_response['result']['parameters']['from_city'])
    to_city = (json_response['result']['parameters']['to_city'])
    if not from_city:
        from_city = default_from_city
    webbrowser.open('https://www.google.co.in/maps/dir/' + from_city + '/' + to_city)


def near_me(json_response):
    latitude, longitude = 16.7852706, 80.8270381  # of nuzividu
    things = (json_response['result']['parameters']['things'])
    url = 'https://www.google.co.in/maps/search/' + things + '/@' + str(latitude) + ',' + str(longitude) + ',14z/'
    webbrowser.open(url)


def locate_me(json_response):
    default_location = 'IIIT Nuzvid'  # todo: get current location
    latitude, longitude = 16.7913671, 80.818628  # of iiit nuzvid
    print('You are at ' + default_location)
    print('Press 1 to show you on Google Maps')
    user_input = int(input())
    if user_input == 1:
        url = 'https://www.google.co.in/maps/search/' + default_location + '/@' + str(latitude) + ',' + str(longitude)
        webbrowser.open(url)
