import os

'''
    -> Write a program to clear the clutter inside a folder on your computer.
    You should use os module to rename all the png images from 1.png all the
    way till n.png where n is the number of png files in that folder. Do the same
    for other file formats. For example: sfdsf.png --> 1.png vfsf.png --> 2.png
    this.png --> 3.png design.png --> 4.png name.png --> 5.png
'''


def clutter(file_ext):
    i = 1
    folder_list = os.listdir("folder")
    for file in folder_list:
        if file.endswith(file_ext):
            os.rename(f"folder/{file}", f"folder/{i}{file_ext}")
            i += 1


if (not os.path.exists("folder")):
    os.mkdir("folder")

for i in range(0, 25):
    if (not os.path.exists(f"folder/jeremiah{i+1}.txt")):
        os.mkdir(f"folder/jeremiah{i+1}.txt")
    if (not os.path.exists(f"folder/conrad{i + 1}.png")):
        os.mkdir(f"folder/conrad{i + 1}.png")
    if (not os.path.exists(f"folder/belly{i + 1}.jpeg")):
        os.mkdir(f"folder/belly{i + 1}.jpeg")

a = input("Enter any one of the file formats given below to edit the file names numerically:\nA].png\t\t B].txt\t\tC].jpeg\n")
clutter(a)
