import asyncio
import sys

from workflow import CertificateGeneratorWorkflow
from temporalio.client import Client


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    handle = await client.start_workflow(
        CertificateGeneratorWorkflow.run,
        sys.argv[1],
        id="generate-certificate-workflow",
        task_queue="generate-certificate-taskqueue",
    )

    print(f"Started workflow. Workflow ID: {handle.id}, RunID {handle.result_run_id}")

    result = await handle.result()

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
