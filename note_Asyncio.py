try:
    import os
    import sys
    import asyncio
    from queue import Queue
    print("{} ".format(sys.version))
except Exception as e:
    print("Some modules are missing : {} ".format(e))
 
square = Queue()
 
 
async def compute_square(num):
    print("computing square : {} ".format(num))
    await asyncio.sleep(3)
    print("Square of Number is : {} ".format(num*num))
    square.put(num*num)
 
 
 
async def compute_cube(num):
    print("computing cube : {} ".format(num))
    await asyncio.sleep(3)
    print("Square of Number is : {} ".format(num * num * num))
    return num* num * num
 
 
async def main():
 
    task1 = asyncio.create_task(coro=compute_square(33))
    await task1
 
    while True:
        flag = square.empty()
        if flag:
            pass
        else:
            response = square.get()
            print(response)
            break
 
    #task2  = asyncio.create_task(coro=compute_cube(33))
 
    # try:
    #
    #     await asyncio.wait_for(task1, timeout=1)
    # except Exception as e:
    #     pass
 
    # response = await task1
    #await task2
 
 
if __name__ == "__main__":
    asyncio.run(main())
