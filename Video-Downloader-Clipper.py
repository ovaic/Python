# Python-Video_Downloader_Clipper

import os
import pandas as pd
from moviepy.editor import *
import pytube 
from pytube import YouTube

df = pd.read_csv(r'C:\Users\awais\links.csv') # read and load csv (Excel) file

# Extracting data in the form og lists
links = df['full_links'].tolist()
time_start = df['time_start'].tolist()
time_end = df['time_end'].tolist()

# loop 
t = 0
for i in links:
    try:
        print(i, time_start[t], time_end[t]) # printing start & end time of videos to be clipped
        youtube = YouTube(i)
        video = VideoFileClip(youtube.streams.first().download()) # Downloading video
        
        # since INTERVAL in dataset for clipping is set to 10 seconds therfore if-else statement for videos smaller then 10 seconds
        if int(video.duration) <= time_end[t]: # videos smaller than 10 seconds
            video = video.subclip(time_start[t],int(video.duration)) # CLIPPING video ... end_time set to max video duration
            t = t + 1
            frames = video.fps
            video.write_videofile(f'{os.getcwd()}\\clipped\\{t}.mp4', fps = frames) # Saving clipping video in "clipped" folder
        else if time_start[t] > int(video.duration):
            video = video.subclip(0, int(video.duration)
            t = t + 1
            frames = video.fps
            video.write_videofile(f'{os.getcwd()}\\not clipped\\{t}.mp4', fps = frames)
        else:
            video = video.subclip(time_start[t],time_end[t])
            t = t + 1
            frames = video.fps
            video.write_videofile(f'{os.getcwd()}\\clipped\\{t}.mp4', fps = frames)
    except Exception as e: 
        print(e) 
        t = t + 1
    
