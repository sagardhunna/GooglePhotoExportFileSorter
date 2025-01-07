import os
import shutil

origin = "/Users/sagardhunna/Desktop/Google Photos BackUp Till 10:14:2024/"
target = "/Users/sagardhunna/Desktop/GooglePhotos/"

dir_list = os.listdir(origin) # Contains all Takeout Folders

print(f'Amount of takeout folders is: {len(dir_list)}')

# Within each takeout folder there is another folder called 'Google Photos' in which there are multiple other folders 
# with the pictures and videos in them, so we can just directly access that main folder within the takeout folder

# NEW ISSUE ENCOUNTERED: Since this is 200 GB of data, copying the files from one spot to another led to 
# running out of storage, so I was only able to copy 7/20 of the take out files at once, so now I will delete the first 
# seven and then continue on

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
                    original_source_to_file = origin + source + '/' + folder + '/' + file
                    shutil.copy(original_source_to_file, target + file)
                        #Only need the following code when testing to figure out where I stopped copying files
                    if file.lower() not in all_files:
                        print(f'We are in {main_folder}/{folder}/{file} and this file doesnt exist')
                        quit()
                    else:
                        continue
            else:
                print(f'{folder} is a file')

print(f'Total files is: {total_files}')
