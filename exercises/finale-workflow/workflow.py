from datetime import timedelta
from temporalio import workflow


@workflow.defn
class CertificateGeneratorWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        out_file_path = await workflow.execute_activity(
            "CreatePdf", name, start_to_close_timeout=timedelta(seconds=5)
        )

        return out_file_path
