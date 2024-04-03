import asyncio

async def fetch_data(url):
    print(f"Started fetching data... for {url}")
    #simulate delay
    await asyncio.sleep(4)
    print(f"Completed : {url}")
    return url

async def main():
    #creating task 
    task1 =  asyncio.create_task(fetch_data("bhandarikapil.com.np"))
    task2 = asyncio.create_task(fetch_data("bhandarikapi.com.np/projects"))

    result1 = await task1
    result2 = await task2

    print(f"Task1 result : {result1}")
    print(f"Task2 result : {result2}")
    print("Complete main function")


asyncio.run(main())
