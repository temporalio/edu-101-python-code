import asyncio
import sys

from greeting import GreetSomeone
from temporalio.client import Client


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        GreetSomeone.run, sys.argv[1], id="greeting-workflow", task_queue="greeting-tasks"
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())