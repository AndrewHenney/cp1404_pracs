
import shutil
import os


def main():
    extensions={}
    os.chdir('FilesToSort')

    for filename in os.listdir('.'):
        name, extension = filename.split('.')
        if (extension in extensions):
            shutil.move(filename, extensions[extension])
        else:
            folder_name=input('What category would you like to sort {} files into?'.format(extension))

            if (folder_name in extensions.values()):
                shutil.move(filename, folder_name)
            else:
                os.mkdir(folder_name)
                shutil.move(filename, folder_name)
            extensions[extension] = folder_name

main()

