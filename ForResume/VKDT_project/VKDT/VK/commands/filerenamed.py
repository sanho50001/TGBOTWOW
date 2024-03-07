import os


def renamed(filename):
    print(filename)
    os.rename(filename, filename[:-3] + 'old.jpg')

