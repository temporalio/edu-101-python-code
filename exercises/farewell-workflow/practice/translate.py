import urllib.parse
from temporalio import activity


class TranslateActivities:
    def __init__(self, session):
        self.session = session

    @activity.defn
    async def greet_in_spanish(self, name: str) -> str:
        greeting = await self.call_service("get-spanish-greeting", name)
        return greeting

    # TODO: write an Activity method that calls the microservice to
    # get a farewell message in Spanish. It will be identical to the
    # method above, except the first argument to the callService
    # method will be "get-spanish-farewell". You can name your
    # method whatever you like.

    # Utility method for making calls to the microservices
    async def call_service(self, stem: str, name: str) -> str:
        base = f"http://localhost:9999/{stem}"
        url = f"{base}?name={urllib.parse.quote(name)}"

        async with self.session.get(url) as response:
            response.raise_for_status()
            return await response.text()
