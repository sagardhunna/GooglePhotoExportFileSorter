import os
import shutil

origin = "/Users/sagardhunna/Desktop/PracticeFolder/"
target = "/Users/sagardhunna/Desktop/PracticeFolder2/"

dir_list = os.listdir(origin)


for file in dir_list:
    if file == ".DS_Store":
        continue
    else:
        shutil.copy(origin+file, target+file)
        # This will copy the file from origin, to target, and will ensure no duplicates
        # The way it works is that if there is a file with the same name, it will just overwrite it

