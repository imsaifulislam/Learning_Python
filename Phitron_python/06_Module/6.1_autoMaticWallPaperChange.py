""" # => Import Required Module
import os
import random
import ctypes

# => Specifying path of the Wallpapers folders
paths = r"C:\Users\saifu\Downloads\WallPaper"

# => Getting list of files from the folder
wallpapers = os.listdir(paths)

# => Remove Unnecessary Files from the FOlder

final_Wallpaper = []
for wall in wallpapers:
    if ".ini" not in wall:
        final_Wallpaper.append(wall)


# => Selecting a random wallpaper
random_wallpaper = final_Wallpaper[random.randint(0,len(final_Wallpaper)-1)]

# => Getting Absolute Path of The Selected Wallpaper
random_wallpaper = os.path.join(paths,random_wallpaper)

# 

random_wallpaper = bytes(random_wallpaper, "utf-8")
ctypes.windll.user32.SystemParametersInfoW(20,0,random_wallpaper,3) """

# ==============================================================================

import subprocess
import wget
import requests
import ast
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import shutil
import os

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
r = requests.get(url)
data = ast.literal_eval(r.content.decode('utf-8'))
print(data["url"])
wget.download(data["url"], "F:\\Programming\\Python\\03_Practice\\Phitron_python\\06_Module\\wallpaper_prev.jpg")