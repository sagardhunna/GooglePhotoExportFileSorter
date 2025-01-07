import os
import shutil

origin = "/Users/sagardhunna/Desktop/Google Photos BackUp Till 10:14:2024/"
target = "/Users/sagardhunna/Desktop/GooglePhotos/"

dir_list = os.listdir(origin) # Contains all Takeout Folders

print(f'Amount of takeout folders is: {len(dir_list)}')

# Within each takeout folder there is another folder called 'Google Photos' in which there are multiple other folders 
# with the pictures and videos in them, so we can just directly access that main folder within the takeout folder

all_files = os.listdir(target)

total_files = 0

for main_folder in dir_list:
    if main_folder.lower() == ".ds_store":
        continue
    else:
        source = main_folder + '/' + 'Google Photos'
        take_out_dir_list = os.listdir(origin + source)
        print(origin + source)
        for folder in take_out_dir_list:
            if os.path.isdir(origin + source + '/' + folder):
                print(f'{folder} is a folder')
                folder_with_files = os.listdir(origin + source + '/' + folder)
                print(f'{folder} contains {len(folder_with_files)}')
                total_files += len(folder_with_files)

                for file in folder_with_files:
                    if file.lower() not in all_files:
                        print(f'We are in {main_folder}/{folder}/{file} and this file doesnt exist')
                        quit()
                    else:
                        continue
                    '''
                    original_source_to_file = origin + source + '/' + folder + '/' + file
                    shutil.copy(original_source_to_file, target + file)
                    '''
            else:
                print(f'{folder} is a file')

print(f'Total files is: {total_files}')
