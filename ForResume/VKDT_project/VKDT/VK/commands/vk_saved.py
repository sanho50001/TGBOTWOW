from dotenv import load_dotenv
import os
import vk
import requests
load_dotenv()


class VKSaved:
    def __init__(self):
        self.requests = requests

    def saved(self, photo_name):

        # Задаём идентификатор группы, токен доступа, картинку и её описание
        group_id = os.getenv('group_id')
        access_token = os.getenv('access_token5')

        # Авторизуемся в VK
        session = vk.Session(access_token=access_token)

        vkapi = vk.API(session=session)

        upload_url = vkapi.photos.getWallUploadServer(group_id=group_id, v=5.131)['upload_url']\

        requests = self.requests.post(upload_url, files={'file': open(photo_name, 'rb')})

        save_wall_photo = vkapi.photos.saveWallPhoto(group_id=group_id,
                                                     v=5.131,
                                                     photo=requests.json()['photo'],
                                                     server=requests.json()['server'],
                                                     hash=requests.json()['hash'])

        saved_photo = 'photo' + str(save_wall_photo[0]['owner_id']) + '_' + str(save_wall_photo[0]['id'])
        vkapi.wall.post(owner_id='-192102262', v=5.131, attachments=saved_photo)

        return photo_name