import asyncio

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

from workflow import CertificateGeneratorWorkflow


async def main():
    client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    worker = Worker(
        client,
        task_queue="generate-certificate-taskqueue",
        workflows=[CertificateGeneratorWorkflow],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
