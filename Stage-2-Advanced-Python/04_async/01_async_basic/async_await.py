import asyncio

async def boil_water():
    print("Put the kettle on...")
    await asyncio.sleep(2)
    print("The water is ready!")

async def main():
    await boil_water()

if __name__ == "__main__":
    asyncio.run(main())