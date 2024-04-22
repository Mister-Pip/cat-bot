import requests
from some_API import RAND_FACT_API

url = "https://random-cat-fact.p.rapidapi.com/"

headers = {
    "X-RapidAPI-Key": RAND_FACT_API,
    "X-RapidAPI-Host": "random-cat-fact.p.rapidapi.com"
}


def get_fact():
    response = requests.get(url, headers=headers)
    result = response.json()["fact"]

    return result


