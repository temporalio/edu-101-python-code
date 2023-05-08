import sys
import asyncio
from workflow import GreetSomeone


async def main():
    name = sys.argv[1]
    greeter = GreetSomeone()
    greeting = await greeter.run(name)
    print(greeting)

if __name__ == "__main__":
    asyncio.run(main())