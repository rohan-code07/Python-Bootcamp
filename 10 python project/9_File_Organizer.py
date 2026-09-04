import os

def arrangement(files, ext):
    file_with_ext = [file for file in files if file.endswith(ext)]
    print(file_with_ext)
    if not(os.path.exists("images")):
        os.mkdir("images")
    for i, file in enumerate(file_with_ext, start=1):
        os.rename(file, f"images/photos-{i}.{ext}")

if __name__ == "__main__":
    files = os.listdir()     
    arrangement(files, ".jpg")   


import os
import shutil
def arrangement(files, ext):
    file_with_ext = [file for file in files if file.endswith(ext)]
    print(file_with_ext)
    if not(os.path.exists("PDF")):
        os.mkdir("PDF")
    for i, file in enumerate(file_with_ext, start=1):
        if file.endswith(ext):
            shutil.move(file, os.path.join("PDF", file))

if __name__ == "__main__":
    files = os.listdir()     
    arrangement(files, ".pdf")   
