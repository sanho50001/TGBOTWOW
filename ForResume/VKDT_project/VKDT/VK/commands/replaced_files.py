import os


def replaced_files(dir_file, dir_outdoing, dir_files_downloading):
    # Проходим по списку файлов из папки выгрузки и переносим их в папку отгрузки
    for file in dir_file:
        if not os.path.isfile(os.path.join(dir_outdoing, file)):
            if not file.endswith('old.jpg'):
                os.replace(os.path.join(dir_files_downloading, file), os.path.join(dir_outdoing, file))


    return print(os.listdir(os.chdir(dir_outdoing)))


def replaced_file(dir_outdoing, dir_files_downloading, file):
    os.replace(os.path.join(dir_files_downloading, file), os.path.join(dir_outdoing, file))
    return
