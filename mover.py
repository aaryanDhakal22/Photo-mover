#! /usr/bin/python3
import os
import shutil
path = "/home/aaryan/"
downloads = os.listdir(path+'Downloads')

for item in downloads:
    if item.endswith("_n.jpg") or (item.endswith(".mp4") and item.startswith("video-") )or  (item.startswith("audioclip-") and item.endswith(".mp4")):
        shutil.move(path+'Downloads/'+item,path+'Pictures/.Ebsi/')

duration = 0.1  # seconds
freq = 400  # Hz
os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))