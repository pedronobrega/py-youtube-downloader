import os
from pytube import YouTube

if not os.path.exists("download"):
    os.mkdir("download")

link = input("Insert URL: ")
video = YouTube(link)
stream = video.streams \
    .filter(progressive=True, file_extension='mp4') \
    .order_by('resolution') \
    .desc()\
    .first() \
    .download("./download/")
