import asyncio

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

from translate import greet_in_spanish
from greeting import GreetSomeone

async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    worker = Worker(
        client, 
        task_queue="greeting-tasks", 
        workflows=[GreetSomeone],
        activities=[greet_in_spanish],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
