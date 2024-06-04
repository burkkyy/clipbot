#!/usr/bin/env python

# Currently broken code, do not use.

# Internal modules
import concurrent.futures
import sys
import os
import json
import re

# Externel modules
from yt_dlp import YoutubeDL
from yt_dlp import DownloadError
from bs4 import BeautifulSoup as bs
import requests as req

# My modules
from clipbot_core import console
from clipbot_core import cache

OUTPUT_PATH = os.path.join(os.getcwd(), 'channels')

def get_metadata(url : str) -> dict:
    """downloads metadata from a url to a youtube channel.
    This works by using the yt-dlp library, which is
    an extension of the youtubedl library.
    Link to yt-dlp github: https://github.com/yt-dlp/yt-dlp

    Args:
        url (str): link to the channel to download

    Returns:
        dict: metadata of the channel
    """    
    console.update(f"Downloading metadata from {url}")

    params = {
        "extract_flat": "in_playlist",
        "dump_single_json": True,
        "quiet": True,  # Set to false for verbose output
    }

    try:
        sys.stderr = open(os.devnull, 'w')  # To hide yt-dlp stderr
        with YoutubeDL(params) as ydl:
            data = ydl.extract_info(url, download=False)    # false, as to not download the video itself
        sys.stderr = sys.__stderr__
    except DownloadError as e:
        console.err(f"Invalid url: '{url}'")
    
    return data


def get_channel_info(url : str) -> str:
    """gets metadata of a channel

    Args:
        url (str): link to the channel

    Returns:
        str: path the channel data was saved to
    """
    # check cache, as to not redownloaded the link
    if cache.check(url):
        console.info(f"Channel '{os.path.basename(url)}' is already downloaded")
        return cache.get_path(url)
    
    metadata = get_metadata(url)
    
    channel_name = metadata['uploader']
    path = os.path.join(OUTPUT_PATH, channel_name, f"{channel_name}.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, "w") as f:
        json.dump(metadata, f)
    
    # Note of this download to cache
    console.info(f"Writing {channel_name} to cache...")
    cache.add(os.path.dirname(path), channel_name, url)
    
    return path


def get_video_titles(url: str) -> None:
    """gets title of every video uploaded by a channel

    Args:
        url (str): link to the channel
    """
    try:
        if cache.get_titles(url):
            console.info(f"Titles from channel at '{url}' are already downloaded.")
            return
        path = cache.get_path(url)
    except KeyError:
       path = get_channel_info(url)
    
    titles_path = os.path.join(path, "titles.csv")
    channel_info = cache.get(url)
    channel_name = channel_info['uploader']
    metadata_path = os.path.join(channel_info['path'], f"{channel_name}.json")
    
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    
    with open(titles_path, 'w') as f:
        if metadata['playlist_count'] > 3:
            for data in metadata['entries']:
                f.write(data['id'])
                f.write('\n')
        else:
            for data in metadata['entries'][0]['entries']:
                f.write(data['id'])
                f.write('\n')

    cache.set_titles(url, True)
    
'''
def get_videos_info(url: str) -> None:
    """gets the json of every video of a channel

    Args:
        url (str): link to a youtube channel
    """
    try:
        if not cache.get_titles(url):
            console.info(f"All videos from channel '{url}' have their json files downloaded")
            return
        path = cache.get_path(url)
    except KeyError:
        path = get_video_titles(url)
        
    videos_info_path = os.path.join(path, 'videos')
    titles_path = os.path.join(path, 'titles.csv')
    base_url = 'https://www.youtube.com/watch?v='
    
    params ={
        "format": "bestaudio/best",
        "quiet": True,
        "no_warnings": True,
        "simulate": True,
        "dump_single_json": True,
        "writeinfojson": True,
        "outtmpl": "temp.mp3"
    }
    
    with open(titles_path, 'r') as f:
        for l in f:
            r = req.get(base_url + l)
            print(base_url + l, end=' ')
            print(r.status_code)
            soup = bs(r.text, 'html.parser')
            found = soup.find(class_='ytp-heat-map-chapter')
            print(found)
'''

def get_playback_data(url: str) -> None:
    """Gets playback data from ever video on a youtube channel

    Args:
        url (str): link to a youtube channel we will get the playback data from
    """
    try:
        if cache.get_playback(url):
            console.info(f"Titles from channel at '{url}' are already downloaded.")
            return
        path = cache.get_path(url)
    except KeyError:
       path = get_channel_info(url)
    
    print(path)

''' Testing '''
if __name__ == '__main__':
    '''
    urls = ('https://www.youtube.com/@davidbulay', 'https://www.youtube.com/@JackRhysider', 'https://www.youtube.com/@MentalOutlaw')
    for url in urls:
        path = get_channel_info(url)
        get_video_titles(url)
        get_playback_data(url)
    
    get_videos_info(urls[0])
    
    url = 'https://www.youtube.com/watch?v=8ZvkaOV82tc'
    
    r = req.get(url)
    soup = bs(r.content, 'html.parser')
    for script in soup.findAll('script'):
        if "decorationTimeMillis" in str(script):
            split = str(script).split("\"decorationTimeMillis\"")[1]
            print(split[1:].split(',')[0])
    '''

    path_to_links = R'C:\Users\caleb\source\repos\clipbot\clipbot_core\data\channels\David Bulay\titles.csv'
    base_url = 'https://www.youtube.com/watch?v='
    
    with open(path_to_links, 'r') as f:
        for n in f:
            url = base_url + n
            response = req.get(url)
            print(f"{response.status_code} {response.url}")
            
            soup = bs(response.content, 'html.parser')
            script = soup.find('script', text=re.compile('decorationTimeMillis'))
            if not script:
                continue
            match = re.search(r'"decorationTimeMillis":\s*(\d+)', script.string)
            if match:
                print(match.group(1))
    
    exit(0)
    
    response = req.get(url)
    soup = bs(response.content, 'html.parser')

    script = soup.find('script', text=re.compile('decorationTimeMillis'))
    match = re.search(r'"decorationTimeMillis":\s*(\d+)', script.string)
    
    if match:
        decoration_time = match.group(1)
        print(decoration_time)
    else:
        print('decorationTimeMillis not found in script')
        exit(0)
    
    seconds, milliseconds = divmod(int(decoration_time), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    
__all__ = ['get_channel_info', 'get_video_titles']
