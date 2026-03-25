import aiohttp
import asyncio
import time

URLS = [
    "https://example.com",
    "https://www.iana.org/domains/reserved",
    "https://catfact.ninja/fact",
    "https://dog.ceo/api/breeds/image/random"
]

async def load_data(session, url):
    print(f"Start loading: {url}")
    async with session.get(url) as response:
        data = await response.text()
        print(f"Finished loading: {url}")
        return {"url": url, "length": len(data)}

async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(load_data(session, url) for url in URLS))

    print("\nResults:")
    for item in results:
        print(f"{item['url']} -> {item['length']} characters")

    print(f"\nTotal time: {round(time.time() - start, 2)} sec")

if __name__ == "__main__":
    asyncio.run(main())