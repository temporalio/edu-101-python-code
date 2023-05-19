import requests
import urllib.parse
from typing import Tuple
from temporalio import activity


@activity.defn
async def greet_in_spanish(name: str) -> str:
    base = "http://localhost:9999/get-spanish-greeting?name=%s"
    url = base % urllib.parse.quote(name)

    try:
        resp = requests.get(url)
        translation = resp.text

        if resp.status_code >= 400:
            raise Exception(f"HTTP Error {resp.status_code}: {translation}") 

        return translation
    except Exception as e:
        return f"{e}"
