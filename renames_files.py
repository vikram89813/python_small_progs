import os

def rename_files():
    file_list = os.listdir("/Users/kumarvikram/codes/udacity_python/prank")
    saved_path=os.getcwd()
    os.chdir("/Users/kumarvikram/codes/udacity_python/prank")
    #print(file_list)
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))

    os.chdir(saved_path)

rename_files()
