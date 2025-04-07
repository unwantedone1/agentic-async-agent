import asyncio
from fastapi import FastAPI
from openai import AsyncOpenAI
from tools import get_weather, search_docs
from schemas import tool_schemas

client = AsyncOpenAI()
app = FastAPI()

TOOLS = {
    "get_weather": get_weather,
    "search_docs": search_docs,
}

@app.post("/ask-agent/")
async def ask_agent(query: str):
    response = await client.chat.completions.create(
        model="gpt-4-0613",
        messages=[{"role": "user", "content": query}],
        tools=tool_schemas,
        tool_choice="auto"
    )

    tool_call = response.choices[0].message.tool_calls[0]
    fn_name = tool_call.function.name
    fn_args = tool_call.function.arguments

    tool_result = await TOOLS[fn_name](**eval(fn_args))

    follow_up = await client.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {"role": "user", "content": query},
            response.choices[0].message,
            {"role": "tool", "tool_call_id": tool_call.id, "name": fn_name, "content": str(tool_result)},
        ]
    )

    return {"answer": follow_up.choices[0].message.content}