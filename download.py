from pytube import YouTube
import subprocess
import os
import glob
import sys

url = sys.argv[1]
yt = YouTube(url)

print('Start.')
yt.streams.get_by_itag(140).download("C:/Users/626ca/IdeaProjects/SocketChat/src/spea55")
print('End.')

dir = glob.glob("C:/Users/626ca/IdeaProjects/SocketChat/src/spea55/*.mp4")

name = [n.split('\\')[-1] for n in dir]

with open("C:/Users/626ca/IdeaProjects/SocketChat/src/spea55/links.txt", mode='a', encoding='UTF-8') as f:
    f.write(url + ',' + name[0] + '\n')
    f.flush()
