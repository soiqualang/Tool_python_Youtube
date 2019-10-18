#from __future__ import unicode_literals
import requests
import youtube_dl

""" Make by soiqualang
dothanhlong.org """

def youtube2video(download_path,youtube_url):
    Location = '%s soiqualang_%(extractor)s-%(id)s-%(title)s.%(ext)s'.replace("%s ", download_path)
    ytdl_format_options = {
        'outtmpl': Location
    }
    with youtube_dl.YoutubeDL(ytdl_format_options) as ydl:
         ydl.download([youtube_url])
            
def youtube2mp3(download_path,youtube_url):
    Location = '%s soiqualang_%(extractor)s-%(id)s-%(title)s.%(ext)s'.replace("%s ", download_path)
    ydl_opts = {
        'outtmpl': Location,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
        
def get_listvideo(url):
    #url="https://www.youtube.com/channel/UCIKTHNRRnVP5d8FpDI5YhXQ/videos"
    page = requests.get(url).content
    data = str(page).split(' ')
    item = 'href="/watch?'
    vids = [line.replace('href="', 'youtube.com') for line in data if item in line] # list of all videos listed twice
    #print(vids[0]) # index the latest video
    return vids