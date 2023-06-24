from deepface import DeepFace
import os

Path = './vggface2_test/test'
correct_num = 0
wrong_num = 0
for dirpath, dirnames, filenames in os.walk(Path):
    print('Current Folder Path:', dirpath)
    dirnum = dirpath[-7:]
    print(dirnum)
    for root, dirs, files in os.walk(dirpath):
        if root != dirpath:
            break
        for file in files:
            path = os.path.join(root, file)
            result = DeepFace.find(img_path=path, db_path="./database", enforce_detection=False)
            res_str = result[0]['identity'][0][11:18]
            print(path)
            if res_str == dirnum:
                correct_num += 1
                print("Correct!")
            else:
                wrong_num += 1
                print("Wrong!")
            if wrong_num == 0:
                continue
            print("Correctness: " + str(correct_num * 1.0 / (correct_num + wrong_num * 1.0) * 100.0))
print("Correctness: " + str(correct_num * 1.0 / (correct_num + wrong_num * 1.0) * 100.0))
