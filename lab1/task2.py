from os import path, listdir, mkdir
from sys import argv

params = argv
params.pop(0)

dir = None
files = []
flag = None
for i in range(0, len(params)):
    param = params[i]
    if param == "--dirpath":
        flag = 1
    elif param == "--files":
        flag = 2
    elif flag == 1:
        dir = param
    elif flag == 2:
        files.append(param)

def reportFiles(dir, files = []):
    if dir == None:
        print("Search directory is not specified")
        return
    if not path.exists(dir) or not path.isdir(dir):
        print("Specified directory does not exist")
        return
    if len(files) == 0:
        files = listdir(dir)
        print(f"Всего файлов: {len(files)}")
        filesSize = 0
        for f in files:
            filePath = path.join(dir, f)
            filesSize += path.getsize(filePath)
        print(f"Общий вес: {filesSize/1024} КБ")
    else:
        exist = []
        notExist = []
        for f in files:
            filePath = path.join(dir, f)
            if path.exists(filePath) and path.isfile(filePath): # isfile can be removed if we think that dirs are files too
                exist.append(f)
            else:
                notExist.append(f)

        # Console output
        print("Существующие файлы:")
        if len(exist) == 0:
            print("Отсутствуют")
        else:
            print("\n".join(exist))
        print("Несуществующие файлы:")
        if len(notExist) == 0:
            print("Отсутствуют")
        else:
            print("\n".join(notExist))

        # File output
        if not path.exists("task2"):
            mkdir("task2")
        with open("task2/existing.txt", "w") as output:
            output.write("\n".join(exist))
        with open("task2/not_existing.txt", "w") as output:
            output.write("\n".join(notExist))

reportFiles(dir, files)