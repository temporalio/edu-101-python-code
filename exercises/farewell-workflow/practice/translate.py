import urllib.parse
import requests

from temporalio import activity


class TranslateActivities:

    @activity.defn
    def greet_in_spanish(self, name: str) -> str:
        greeting = self.call_service("get-spanish-greeting", name)
        return greeting

    # TODO: write an Activity method that calls the microservice to
    # get a farewell message in Spanish. It will be identical to the
    # method above, except the first argument to the callService
    # method will be "get-spanish-farewell". You can name your
    # method whatever you like.

    # Utility method for making calls to the microservices
    def call_service(self, stem: str, name: str) -> str:
        base = f"http://localhost:9999/{stem}"
        url = f"{base}?name={urllib.parse.quote(name)}"

        response = requests.get(url)
        return response.text

