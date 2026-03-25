import asyncio
import time


async def coro1():
    print(f"Start coro1")
    await asyncio.sleep(1)
    print(f"Finish coro1")

async def coro2():
    print(f"Start coro2")
    await asyncio.sleep(2)
    print(f"Finish coro2")

async def coro3():
    print(f"Start coro3")
    await asyncio.sleep(3)
    print(f"Finish coro3")

async def main():
    print("=== Time check start ===")
    start_timer = time.time()
    await asyncio.gather(coro1(), coro2(), coro3())
    print(f"Total async time: {round(time.time() - start_timer, 2)} sec")

if __name__ == "__main__":
    asyncio.run(main())
