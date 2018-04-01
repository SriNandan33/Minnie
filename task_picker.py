from modules import (
    webopener,
    maps,
    newsReader,
    )


class TaskIdentifier:
    def open_website(json_response):
        webopener.open_website(json_response)

    def get_directions(json_response):
        maps.get_directions(json_response)

    def near_me(json_response):
        maps.near_me(json_response)

    def locate_me(json_response):
        maps.locate_me(json_response)

    def read_news(json_response):
        newsReader.read_news()
