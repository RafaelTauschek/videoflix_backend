import subprocess
import json


def convert_360p(source):
    if source.endswith('.mp4'):
        target = source.replace('.mp4', '_360p.mp4')
    else:
        target = source + '_360p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd360 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd, shell=True)


def convert_720p(source):
    if source.endswith('.mp4'):
        target = source.replace('.mp4', '_720p.mp4')
    else:
        target = source + '_720p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd, shell=True)

  
def convert_1080p(source):
    if source.endswith('.mp4'):
        target = source.replace('.mp4', '_1080p.mp4')
    else:
        target = source + '_1080p.mp4'
    cmd = 'ffmpeg -i "{}" -s hd1080 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd, shell=True)



def get_video_duration(source):
    cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(source)
    subprocess.run(cmd, shell=True)