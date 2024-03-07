import datetime
import os.path
import time


class Queue:

    def __init__(self):
        self.start = None
        self.saved = None
        self.queue_list = []
        self.last_photo = None
        self.last_time_photo_queue = None
        self.out_queue_list = []

    def set_start(self, start):
        self.start = start

    def set_saved(self, saved):
        self.saved = saved

    def set_last_time_photo_queue(self, time):
        self.last_time_photo_queue = time

    def set_last_photo(self, named_photo):
        self.last_photo = named_photo

    def get_queue_list(self):
        return self.queue_list

    def get_last_time_photo_queue(self):
        return self.last_time_photo_queue

    def get_last_photo(self):
        return self.last_photo

    def queue(self):
        # Достаем все файлы и добавляем в очередь
        self.queue_list.append(self.start.get_dir_file())

    def one(self):
        for photo in self.get_queue_list():
            time.sleep(30 * 60)
            self.last_photo = photo
            self.out_queue_list.append(self.get_last_photo())
            time.sleep(1)
            self.saved.saved(photo_name=self.get_last_photo())
            time.sleep(1)
            self.get_queue_list().remove(self.get_last_photo())
            time.sleep(1)

    def mod_date(self, file):
        t = os.path.getmtime(file)
        return datetime.datetime.fromtimestamp(t)

    def out_queue(self):
        for file in self.start.get_dir_file():
            timed_file = self.mod_date(file)
            print(timed_file)
            if timed_file <= self.get_last_time_photo_queue():
                self.set_last_time_photo_queue(time=timed_file)
                self.set_last_photo(named_photo=file)

            elif self.get_last_photo() == None:
                self.set_last_photo(named_photo=file)


