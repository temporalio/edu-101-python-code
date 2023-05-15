from temporalio import workflow


@workflow.defn
class GreetSomeone:
    @workflow.run
    async def run(self, name: str) -> str:
        return f"Hello {name}!"
