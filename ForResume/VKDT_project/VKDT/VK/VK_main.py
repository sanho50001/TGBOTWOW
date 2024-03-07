# Импортируем необходимые модули
from commands.isdir import isdir
from commands.replaced_files import replaced_files, replaced_file
from commands.maincom import Maincom
from commands.vk_saved import VKSaved
from commands.queue import Queue


class VKontacte():

    def saved_in_vk(self):
        saved.saved(photo_name=queue.get_last_photo())

    def replaced(self, file):
        replaced_file(file=file,
                      dir_outdoing=start.get_dir_outdoing(),
                      dir_files_downloading=start.get_dir_files_downloading())


if __name__ == '__main__':

    # Инициализация команд
    start = Maincom()
    saved = VKSaved()
    queue = Queue()
    vkontacte = VKontacte()

    # Настройка команд
    queue.set_start(start=start)
    queue.set_saved(saved=saved)

    # Действие команд

