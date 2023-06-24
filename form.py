from deepface import DeepFace
import os
import random
from shutil import copyfile

Path = './vggface2_test/test'
for dirpath, dirnames, filenames in os.walk(Path):
    print('Current Folder Path:', dirpath)
    dirnum = dirpath[-7:]
    dir = []
    for root, dirs, files in os.walk(dirpath):
        if root != dirpath:
            break
        for file in files:
            path = os.path.join(root, file)
            dir.append(path)
    num = len(dir)
    if num != 0:
        res = random.sample(range(0, num), 5)
        for i in range(5):
            copyfile(dir[res[i]], "./database/" + dirnum + "_" + str(i) + ".jpg")
            print(dir[res[i]])
