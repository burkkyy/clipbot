#!/usr/bin/env python

# Internal modules
import sys
import os
import json

# Externel modules 
from yt_dlp import YoutubeDL
from yt_dlp import DownloadError

# My modules
import console
import cache

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
    
    base_path = os.path.join(os.getcwd(), "data", "channels")   # where we will store downloaded channels
    
    metadata = get_metadata(url)
    
    channel_name = metadata['uploader']
    path = os.path.join(base_path, channel_name, f"{channel_name}.json")
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
        if cache.have_titles(url):
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
        if metadata['playlist_count'] > 3:
            for data in metadata['entries']:
                print(data['id'])
        else:
            for data in metadata['entries'][0]['entries']:
                print(data['id'])
    
    '''
    with open(titles_path, 'w') as f:
        try:
            for m in metadata['entries'][0][f'{channel_name} - Videos']['entries']:
                ...
        except KeyError:
            print('Error')
        
            for m in metadata['entries']:
                f.write(m['id'])
                f.write('\n')
    '''


def get_playback_data(url: str) -> None:
    """Gets playback data from ever video on a youtube channel

    Args:
        url (str): link to a youtube channel we will get the playback data from
    """    
    ...

''' Testing '''
if __name__ == '__main__':
    urls = ('https://www.youtube.com/@davidbulay', 'https://www.youtube.com/@JackRhysider')
    for url in urls:
        path = get_channel_info(url)
        get_video_titles(url)
    
__all__ = ['get_channel_info']
