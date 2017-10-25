
import shutil
import os


def main():
    extension_list = []
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        name, extension = filename.split('.')
        print(extension)
        if (extension in extension_list):
            shutil.move(filename, extension)
        else:
            extension_list.append(extension)
            os.mkdir(extension)
            shutil.move(filename, extension)




main()