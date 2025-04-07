import httpx
import asyncio

async def get_weather(location: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"https://wttr.in/{location}?format=3")
        return res.text

async def search_docs(query: str):
    await asyncio.sleep(1)
    return f"Search results for '{query}': [doc1, doc2, doc3]"