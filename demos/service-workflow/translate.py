import urllib.parse
from temporalio import activity


class TranslateActivities:
    def __init__(self, session):
        self.session = session

    @activity.defn
    async def greet_in_spanish(self, name: str) -> str:
        base = f"http://localhost:9999/get-spanish-greeting"
        url = f"{base}?name={urllib.parse.quote(name)}"

        async with self.session.get(url) as response:
            response.raise_for_status()
            return await response.text()
