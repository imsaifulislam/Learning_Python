import json
import os
import re
import requests
from tqdm import tqdm
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()
json_file_path = filedialog.askopenfilename(title="Select TXT file", filetypes=[("TXT files", "*.txt")])
if not json_file_path:
    exit()

with open(json_file_path, 'r') as f:
    data = json.load(f)

folder_name = re.sub(r'\W+', '', data['title'])
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

for i, video in enumerate(tqdm(data['videos'])):
    video_name = re.sub(r'\W+', '', video['name'])
    video_m3u8_url = video['link']
    video_mp4_url = video_m3u8_url.replace("/manifest/video.m3u8", "/downloads/default.mp4")
    file_name = f"{i+1:02d}_{video_name}"
    file_name = re.sub(r'\W+', '', file_name)
    mp4_file_path = os.path.join(folder_name, file_name + ".mp4")
    # m3u8_file_path = os.path.join(folder_name, file_name + ".m3u8")
    # if os.path.exists(mp4_file_path) or os.path.exists(m3u8_file_path):
    if os.path.exists(mp4_file_path):
        continue
    try:
        with requests.get(video_mp4_url, stream=True) as response, open(mp4_file_path, 'wb') as f:
            response.raise_for_status()
            file_size = int(response.headers.get('content-length', 0))
            block_size = 1024 * 4
            pbar = tqdm(total=file_size, unit='B', unit_scale=True, desc=f"Downloading {file_name}")
            for chunk in response.iter_content(block_size):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
            pbar.close()
    except requests.exceptions.HTTPError:
        # with requests.get(video_m3u8_url, stream=True) as response, open(m3u8_file_path, 'wb') as f:
        #     response.raise_for_status()
        #     file_size = int(response.headers.get('content-length', 0))
        #     block_size = 1024 * 4
        #     pbar = tqdm(total=file_size, unit='B', unit_scale=True, desc=f"Downloading {file_name}")
        #     for chunk in response.iter_content(block_size):
        #         if chunk:
        #             f.write(chunk)
        #             pbar.update(len(chunk))
        #     pbar.close()