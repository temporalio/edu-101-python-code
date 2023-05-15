from datetime import timedelta
from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    # TODO: import your new Activity here
    # hint: you can just add a , and add your activity function name
    from translate import greet_in_spanish


@workflow.defn
class GreetSomeone:
    @workflow.run
    async def run(self, name: str) -> str:
        greeting = await workflow.execute_activity(
            greet_in_spanish, name, start_to_close_timeout=timedelta(seconds=5)
        )

        # TODO: uncomment the lines below and change it to execute the Activity function you created
        # farewell = await workflow.execute_activity(
        #    greet_in_spanish, name, start_to_close_timeout=timedelta(seconds=5)
        # )

        return f"{greeting}\n{farewell}"
