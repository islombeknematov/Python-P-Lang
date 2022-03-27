from time import sleep
from time import time

import asyncio      # Event loop -> цикл обработки событий
                    #                или диспетчер событий



def loader(url):
    print("Load {}".format(url))


async def spider(site_name):
    for page in range(1, 4):
        await asyncio.sleep(1)      # await -> запускает механизм ожидания и
        print(site_name, page)      # передает управление из функции обратно в even_loop
                                    # чтобы диспетчер мог запустить другие функции
start = time()

# spider('Blog')
# spider('News')
# spider('Contact')

spiders = [
    asyncio.ensure_future(spider("Blog")),
    asyncio.ensure_future(spider("News")),
    asyncio.ensure_future(spider("Contact"))
]

print(spider('Blog'))

event_loop =asyncio.get_event_loop()

loader("url 1")

event_loop.run_until_complete(asyncio.gather(*spiders))

loader("url 2")

event_loop.close()

print("{:.2F}".format(time() - start))



