import asyncio
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIChatModel
from prompt import SYSTEM_PROMPT
import os
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    'openai:gpt-4o-mini',
    name='math-prof',
    system_prompt=SYSTEM_PROMPT,
    instrument=True,
)

@agent.tool_plain
def add_numbers(a: int, b: int) -> int:
    """ Adds two numbers and return the result"""
    return a + b

async def main():
    print("AI Assistant - Type 'exit' to quit")

    conversation_history: list[dict] = []

    while True:
        user_query = input("User: ").strip()

        if not user_query:
            continue

        if(user_query.lower() == "exit"):
            print("Speak to you soon!")
            break

        result = await agent.run(user_prompt=user_query, message_history=conversation_history[-10:])

        conversation_history = result.all_messages()

        print(f"AI: {result.output} \n")



if __name__ == "__main__":
    asyncio.run(main())
