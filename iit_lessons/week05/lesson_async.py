from datetime import datetime
import asyncio

# async def task():
#     print("Starting task")
#     await asyncio.sleep(1)
#     print("Task complete")

# asyncio.run(task())

async def delay():
    this_sec = int(datetime.now().strftime("%S"))
    while True:
        next_sec = int(datetime.now().strftime("%S"))
        if next_sec == 0:
            next_sec = 60
        if this_sec+4 > 60:
            next_sec = next_sec +60
        if next_sec == this_sec + 4:
            print("Four seconds had passed")
            return

async def test1():
    await asyncio.gather(
        delay()
    )
    print("Plump")
    

async def test2():
    print("Function test2 is executed")

async def main():
#     # run_test1 = asyncio.create_task(test1())
#     # await run_test1
#     # test2()
    await asyncio.gather(
        test1(),
        test2()
    )

# main()
asyncio.run(main())