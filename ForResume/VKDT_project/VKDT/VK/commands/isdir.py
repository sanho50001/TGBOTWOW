import os

def isdir(dir_outdoing):
    # Делаем проверку есть ли директория в которую отгружаются файлы, если нет, то создается
    if not os.path.isdir(dir_outdoing):
        os.makedirs(dir_outdoing)
    return