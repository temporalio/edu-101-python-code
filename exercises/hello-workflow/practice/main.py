import asyncio

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

from greeting import GreetSomeone


async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    worker = Worker(
        # TODO: modify the statement below to specify the task queue name
        client,
        task_queue="TODO",
        workflows=[GreetSomeone],
    )
    result = await worker.run()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
