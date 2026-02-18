import asyncio
import time

def sync_boil_water(index):
    print(f"Settle kettle {index}")
    time.sleep(2)
    print(f"Kettle {index} is ready")

async def async_boil_water(index):
    print(f"Start kettle {index}")
    await asyncio.sleep(2)
    print(f"Kettle {index} is ready!")

async def main():
    print("\n--- Synchronous version ---")
    start_sync = time.time()
    for i in range(1, 4):
        sync_boil_water(i)
    print(f"Total sync time: {round(time.time() - start_sync, 2)} sec")

    print("\n--- Asynchronous version ---")
    start_async = time.time()
    await asyncio.gather(async_boil_water(1), async_boil_water(2), async_boil_water(3))
    print(f"Total async time: {round(time.time() - start_async, 2)} sec")

if __name__ == "__main__":
    asyncio.run(main())