from pytube import YouTube
import os
import glob
import sys
import subprocess

url = sys.argv[1].strip()
yt = YouTube(url)

print('Start.')
yt.streams.get_by_itag(140).download("D:/goWork/SocketServer/MusicHolder")
print('End.')

dir = glob.glob("D:/goWork/SocketServer/MusicHolder/*.mp4")
print(dir)
name = [n.split('\\')[-1] for n in dir]
print(name)

with open("D:/goWork/SocketServer/main/links.txt", mode='a', encoding='UTF-8') as f:
    f.write(url + ',' + name[0] + '\n')
    f.flush()

os.chdir(r'C:\Program Files\ffmpeg-20191115-bfa8272-win64-static\bin')
cmd = 'ffmpeg.exe -i  \"{0}\".mp4 \"{0}\".mp3'.format(str(dir[-1].split('.')[0]))

subprocess.call(cmd)
os.remove(dir[-1])
