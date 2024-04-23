import requests

api_url = 'https://api.thecatapi.com/v1/images/search'


def get_pic():

    response = requests.get(api_url).json()
    result = response[0]['url']

    return result
