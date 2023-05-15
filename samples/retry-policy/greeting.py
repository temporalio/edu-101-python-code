from datetime import timedelta
from temporalio import workflow
from temporalio.common import RetryPolicy

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from greeting import greet_someone


@workflow.defn
class GreetSomeone:
    @workflow.run
    async def run(self, name: str) -> str:
        retry_policy = RetryPolicy(
            initial_interval=timedelta(seconds=15),
            backoff_coefficient=2.0,
            maximum_interval=timedelta(seconds=160),
            maximum_attempts=100,
        )
        greeting = await workflow.execute_activity(
            greet_someone,
            name,
            start_to_close_timeout=timedelta(seconds=5),
            retry_policy=retry_policy,
        )

        return f"{greeting}"
