import shutil
import os
import winsound

def mover(location):
    shutil.move(str("C:/Users/Dell/Downloads/"+location),"D:\Study\Ebsi")

downloads = os.listdir("C:/Users/Dell/Downloads")

files = list()

for item in downloads:
    if item.endswith("_n.jpg") or (item.endswith(".mp4") and item.startswith("video-") )or  (item.startswith("audioclip-") and item.endswith(".mp4")):
        files.append(item)

print(files)

for items in files:
    mover(items)

winsound.Beep(399,400)