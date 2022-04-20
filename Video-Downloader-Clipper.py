import sys
import os
import pandas as pd
from moviepy.editor import *
import pytube 
from pytube import YouTube

df = pd.read_csv(r'C:\Users\awais\links.csv')

links = df['full_links'].tolist()
time_start = df['time_start'].tolist()
time_end = df['time_end'].tolist()

t = 0
for i in links:
    try:
        print(i, time_start[t], time_end[t])
        youtube = YouTube(i)
        video = VideoFileClip(youtube.streams.first().download())

        if int(video.duration) <= time_end[t]:
            video = video.subclip(time_start[t],int(video.duration))
            t = t + 1
            frames = video.fps
            video.write_videofile(f'{os.getcwd()}\\clipped\\{t}.mp4', fps = frames)
        else:
            video = video.subclip(time_start[t],time_end[t])
            t = t + 1
            frames = video.fps
            video.write_videofile(f'{os.getcwd()}\\clipped\\{t}.mp4', fps = frames)
    except Exception as e: 
        print(e) 
        t = t + 1
    
