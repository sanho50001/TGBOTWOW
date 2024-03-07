import time
# from celery import shared_task
from VKDT.VKDT.celery import app
from VKDT.VK.VK_main import *


@app.task
def news_task(task_id=1):

    while True:
        print('Начат процесс таска ')
        print()
        print('Отправка в VK')
        file = vkontacte.saved_in_vk()
        print('Пост выложен')
        print()


        vkontacte.replaced(file=file)
        print('Отправка в сон')
        minutes = 30
        secundes = 60
        time.sleep(minutes * secundes)
