import asyncio
import aiohttp
import time

async def fetch_data(session, url):
    async with session.get(url) as response:
        print(f"Fetching: {url}")
        data = await response.text()
        print(f"Done: {url}")
        return len(data)

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://neverssl.com/"
    ]
    start = time.time()

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(fetch_data(session, url) for url in urls))
        print("\nData length:", results)

    print(f"Total time: {round(time.time() - start, 2)} sec")

if __name__ == "__main__":
    asyncio.run(main())





