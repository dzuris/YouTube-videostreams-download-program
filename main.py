import json
from yt_dlp import YoutubeDL

# Load configuration from JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

output_path = config['output_path']

def Download(link, output_path):
    # Specify the output template for saving the file to the given path
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s'   # Saves the video in the specified folder with its title
        }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

link = input("Enter the YouTube video URL: ")
Download(link, output_path)