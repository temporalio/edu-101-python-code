import asyncio
import sys

from workflow import CertificateGeneratorWorkflow
from temporalio.client import Client


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    result = await client.execute_workflow(
        CertificateGeneratorWorkflow.run, sys.argv[1], id="generate-certificate-workflow", task_queue="generate-certificate-taskqueue"
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())