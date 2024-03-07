from VKDT.VKDT.celery import app
from VKDT.VK.VK_main import queue


@app.task
def news_task(task_id=1):
    while True:
        print('Начат процесс таска нахождения файла')
        queue.out_queue()
        print('Завершение')
        break
