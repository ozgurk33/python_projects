from tkinter import *
from tkinter import filedialog
from pytubefix import YouTube
from moviepy.editor import *
import shutil

def download():
    video_path=url_entry.get()
    file_path=path_label.cget('text')
    print('Downloading.....')
    mp4=YouTube.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download()
    video_clip=VideoFileClip(mp4)
    video_clip.close()
    shutil.move(mp4,file_path)
    print('Download complete')

def get_path():
    path=filedialog.askdirectory()
    path_label.config(text=path)

root=Tk()
root.title('Video Downloader')
canvas=Canvas(root,width=600,height=400)
canvas.pack()

app_label=Label(root,text='Video Downloader',fg='blue',font=('Arial',15))
canvas.create_window(300,40,window=app_label)

url_label=Label(root,text='Enter video URL')
url_entry=Entry(root)
canvas.create_window(300,100,window=url_label)
canvas.create_window(300,120,window=url_entry)

path_label=Label(root,text='Select path to download')
path_button=Button(root,text='Select',command=get_path)
canvas.create_window(300,170,window=path_label)
canvas.create_window(300,200,window=path_button)

download_button=Button(root,text='Download',command=download)
canvas.create_window(300,275,window=download_button)


root.mainloop()