from modules import (
    webopener,
    maps,
    newsReader,
    system_apps,
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

    def sys_apps(json_response):
        system_apps.open_app(json_response)

