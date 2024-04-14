import os
import subprocess


def convert_360p(source):
    try:
        target = source.replace('.mp4', '_360p.mp4')
        cmd = 'ffmpeg -i "{}" -vf scale=-1:360 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
        subprocess.run(cmd, capture_output=True, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error converting video to 360p: {e}")


def convert_720p(source):
    try:
        target = source.replace('.mp4', '_720p.mp4')
        cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
        subprocess.run(cmd, capture_output=True, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error converting video to 720p: {e}")


def convert_1080p(source):
    try:
        target = source.replace('.mp4', '_1080p.mp4')
        cmd = 'ffmpeg -i "{}" -s hd1080 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
        subprocess.run(cmd, capture_output=True, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error converting video to 1080p: {e}")


def generate_thumbnail(source, title):
    try:
        thumbnail_dir = os.path.join("media", "thumbnails")
        os.makedirs(thumbnail_dir, exist_ok=True)
        target = os.path.join(thumbnail_dir, f"{title}_thumbnail.png")
        cmd = 'ffmpeg -ss 00:00:15 -i {} -frames:v 1 {}'.format(source, target)
        subprocess.run(cmd, shell=True, check=True)
        return target
    except subprocess.CalledProcessError as e:
        print(f"Error generating thumbnail: {e}")
        return None


def capture_duration(source):
    try:
        cmd = 'ffprobe -i "{}" -show_entries format=duration -v quiet -of csv="p=0"'.format(source)
        duration = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        return int(float(duration))
    except subprocess.CalledProcessError as e:
        print(f'Error capturing duration: {e}')
        return None


