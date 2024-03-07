
# # Задаём идентификатор группы, токен доступа, картинку и её описание
# group_id = os.getenv('group_id')
# access_token = os.getenv('access_token5')
# # filename = open('walp/1.jpg', 'rb')
# # Авторизуемся в VK
# # session = vk.CommunityAPI(access_token=access_token)
# session = vk.Session(access_token=access_token)
#
# vkapi = vk.API(session=session)
# # v = 5.95
#
# upload_url = vkapi.photos.getWallUploadServer(group_id=group_id, v=5.131)['upload_url']\
#
# requests = requests.post(upload_url, files={'file': open(photo_name, 'rb')})
#
# save_wall_photo = vkapi.photos.saveWallPhoto(group_id=group_id,
#                                              v=5.131,
#                                              photo=requests.json()['photo'],
#                                              server=requests.json()['server'],
#                                              hash=requests.json()['hash'])
#
# saved_photo = 'photo' + str(save_wall_photo[0]['owner_id']) + '_' + str(save_wall_photo[0]['id'])
# print(saved_photo)
# vkapi.wall.post(owner_id='-192102262', v=5.131, attachments=saved_photo)



# def isdir(dir_outdoing):
#     # Делаем проверку есть ли директория в которую отгружаются файлы, если нет, то создается
#     if not os.path.isdir(dir_outdoing):
#         os.makedirs(dir_outdoing)
#     return

# def replaced_files(dir_file):
#     # Проходим по списку файлов из папки выгрузки и переносим их в папку отгрузки
#     for file in dir_file:
#         if not os.path.isfile(os.path.join(dir_outdoing, file)):
#             if not file.endswith('old.jpg'):
#                 os.replace(os.path.join(dir_files_downloading, file), os.path.join(dir_outdoing, file))
#
#
#     return print(os.listdir(os.chdir(dir_outdoing)))
# start = Startcom()
# saved = VKSaved()
# # Делаем проверку на папку
# isdir(dir_outdoing=start.get_dir_outdoing())
# Делаем проверку на папку
# isdir(dir_outdoing=start.get_dir_outdoing())
# # Узнаем сегоднешнию дату
# time_data = datetime.date.today()
#
# # Узнаем в какой директории была запущенна программа
# cur_dir = str(os.getcwd())
#
# # Из директории обращаемся к папке с фото
# from_file = os.chdir('walp')
#
# # Достаем список всех файлов в папке
# dir_file = os.listdir(from_file)
#
# # Указываем папку выгрузки файлов
# dir_files_downloading = os.path.join(cur_dir, 'photo')
#
# # Указываем папку отгрузки файлов
# dir_outdoing = os.path.join(cur_dir, 'Outdoing', 'PhotoDay', str(time_data))


# # Достаем все файлы и добавляем в очередь
# queue = []
#
# start.get_dir_file()


# Загрузка фото


#
# # Проводим перекидывание файлов
# replaced_files(
#     dir_file=start.get_dir_file(),
#     dir_outdoing=start.get_dir_outdoing(),
#     dir_files_downloading=start.get_dir_files_downloading()
# )
