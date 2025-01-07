There are 20, 10 GB folders of a mixute of images and videos

Images with format .HEIC/.heic have an associated TIFF file with meta data regarding Date Time

Images with format .PNG have an associated Exif file with meta data regarding Date Time Original

Images with format .JPG have an associated TIFF file with meta data regarding Date Time

Some .PNG files do not have any associated files with meta data, however JSON files do exist with the exact same name
For example, if the .png file is 'schedule.png', then the associated json file is 'schedule.png.json'

Videos with format .MOV have an associated .json file with the exact same date containing meta data

Videos with format .MP4 sometimes have an associated file, sometimes don't

The goal to find the date for files without a TIFF or Exif file 
is to create a dictionary where keys are the original file and values are the associated json files

For the files with a TIFF or Exif file, goal is to access their metadata to get the information regarding the date and time

Once retrieving all the Date and Time information for every file, I want to rename every single file and json file to be
the date and time I retreived from the file, EXAMPLE:

Lets say File_A's date is 09/23/2022 and time is 15:29
Then I would change the File_A's name to be 202209231529, and lets say File_B's date and time were
09/23/2022 and time is 12:45 then File_B's name would be 202209231245 and in the file explorer, if you sort by name
File_B would come before File_A as it's value is less

This would then result in files being in reverse order, from the first image you ever took to the most recent
