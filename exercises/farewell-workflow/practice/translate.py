import requests
import urllib.parse
from typing import Tuple
from temporalio import activity


@activity.defn
async def greet_in_spanish(name: str) -> str:
    greeting = call_service("get-spanish-greeting", name)
    return greeting


# TODO: write an Activity function that calls the microservice to
# get a farewell message in Spanish. It will be identical to the
# function above, except the first argument to the callService
# function will be "get-spanish-farewell". You can name your
# function whatever you like.


# Utility function for making calls to the microservices
def call_service(stem: str, name: str) -> str:
    base = "http://localhost:9999/" + stem + "?name=%s"
    url = base % urllib.parse.quote(name)

    try:
        resp = requests.get(url)
        translation = resp.text

        if resp.status_code >= 400:
            raise Exception(f"HTTP Error {resp.status_code}: {translation}")

        return translation
    except Exception as e:
        return f"{e}"
