""" import requests
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"


response = requests.get(api_url)

# -> Get Json
# content = response.content
content = response.content.decode('UTF-8')
# print(type(content))
# print(content)


# Cpnvert String To json

dict_content = json.loads(content)
# print(type(dict_content))
# print(dict_content)


# get the image url
# img_url = dict_content['url']
img_url = dict_content['https://picsum.photos/200/300']
print(img_url)

# download the image
res = requests.get(img_url)
# print(res)

# seve The image
with open('apod.png','wb') as image:
    image.write(res.content)
    
    
# set as wallpaper
# PyWallpaper.change_wallpaper('F:\Programming\Python\03_Practice\Phitron_python\06_Module\apod.png') """



""" import PyWallpaper
PyWallpaper.change_wallpaper('https://picsum.photos/200/300') """

""" 
    * Import Requests Module For Download Images
    * Respons 200 |> Everyting Is Ok
    * Uft-8 to Decode
"""

# ---------------------------------------------------------------------

import requests
import json
import ctypes

# => Get Api
api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# => Get Json
response = requests.get(api_url)
# content = response.content
content = response.content.decode('UTF-8')

# print(type (content))
# print(content)

# => Convert string to json
dict_content = json.loads(content)
# print(type(dict_content))

# => Get The image URL
image_url = dict_content['url']
print(image_url)


# => download Image
save_image = requests.get(image_url)
# print(save_image)

# => Save The Image
with open('F:\\Programming\\Python\\03_Practice\\Phitron_python\\06_Module\\apods.png','wb') as image:
    image.write(save_image.content)


# => use Wallpaper
wallper_path = 'F:\\Programming\\Python\\03_Practice\\Phitron_python\\06_Module\\apods.png'
ctypes.windll.user32.SystemParametersInfoW(40,0,wallper_path,3)