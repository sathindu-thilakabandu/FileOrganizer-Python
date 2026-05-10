import os
import shutil

#now we need to define the directory to organize
#create a new variable called target_dir and assign the directory path to it

target_dir = r"C:\Users\Sathindu\Downloads\Wallpaper"

#define the categories and their extensions

extensions = {
    "Images":[".jpg",".jpeg",".png",".gif"],
    "Videos":[".mp4",".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi"],

}

def organize_folder():
    #Loop through all files in the directory
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir,filename)

        #skip if it's a directory
        if os.path.isdir(file_path):
            continue

        #get the extension
        file_ext = os.path.splitext(filename)[1].lower()

        #Move the file based on its extension
        for folder,ext_list in extensions.items():
            if file_ext in ext_list:
                dest_folder = os.path.join(target_dir,folder)

                #create the folder if it doesn't exists
                os.makedirs(dest_folder, exist_ok=True)

                #move file

                shutil.move(file_path,os.path.join(dest_folder,filename))
                print(f"Moved:{filename}->{folder}")

if __name__ =="__main__":
    organize_folder()
