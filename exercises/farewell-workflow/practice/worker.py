import asyncio
import aiohttp

from temporalio.client import Client
from temporalio.worker import Worker

from translate import TranslateActivities
from greeting import GreetSomeone


async def main():
    client = await Client.connect("localhost:7233", namespace="default")

    # Run the worker
    async with aiohttp.ClientSession() as session:
        activities = TranslateActivities(session)

        worker = Worker(
            client,
            task_queue="greeting-tasks",
            workflows=[GreetSomeone],
            # TODO register your new activity below
            activities=[activities.greet_in_spanish],
        )
        print("Starting the worker....")
        await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
