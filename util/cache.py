#!/usr/bin/env python

'''
@file util/cache.py
@author Caleb Burke
@date 2024-02-12

Caching for clipbot.

Currently broken code, do not use.

'''

# Internal modules
import json

# My modules
<<<<<<<< HEAD:clipbot_old/cache.py
import console
========
from util import console
>>>>>>>> dev-caleb:util/cache.py

# relative path of where the cache will be stored, go nuts with this
CACHE_PATH = "cache.json"

def init() -> None:
    console.update("Creating cache...")
    cache = {
        "channels": []
    }
    write(cache)


def read() -> dict:
    try:
        with open(CACHE_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        console.info("No cache found.")
        init()
        return read()


def write(cache: dict) -> None:
    with open(CACHE_PATH, 'w') as f:
        json.dump(cache, f, indent=4)


def clear() -> None:
    console.info("Cleaning cache...")
    init()


def add(path: str, uploader: str, url: str) -> None:
    """Notes of a download to cache

    Args:
        path (str): the path to the downloaded data\n
        uploader (str): name of downloaded channel\n
        url (str): link to the youtube channel
    """
    console.print_warnings(False)   # turn off warning message for the check call
    if check(url):
        console.print_warnings(True)
        console.warning(f"Channel name '{uploader}' is already in cache")
        return
    console.print_warnings(True)
    
    cache = read()
    data = {
        "uploader": uploader,
        "url": url,
        "path": path,
        "titles": False,
        "playback": False
    }
    cache['channels'].append(data)
    write(cache)


def get(url: str) -> dict:
    """helper func for the other get functions

    Args:
        url (str): link to youtube channel

    Returns:
        dict: channel data
    """
    cache = read()
    if len(cache) == 0: # could also do bool(cache) but this is clearer
        return False

    for channel in cache['channels']:
        if url == channel['url']:
            return channel
    
    console.error(f"The url '{url}' was not found in cache")
    raise KeyError


def get_path(url: str) -> str:
    """Gets a path to a downloaded url

    Args:
        url (str): the web address of the downloaded data

    Returns:
        str: absolute path to the folder with the channel data
    """
    channel = get(url)
    return channel['path']


def check(url: str) -> bool:
    """Checks if a url is already downloaded

    Args:
        url (str): link to a youtube channel

    Returns:
        bool: if channel is downloaded
    """
    try:
        for channel in read()['channels']:
            if url == channel['url']:
                return True
        
    except KeyError:
        console.error(f"Formatting error in cache.")
    
    console.warning(f"The url '{url}' was not found in cache.")
    return False


def get_titles(url: str) -> bool:
    """Checks if the titles of a channel are already downloaded

    Args:
        url (str): link to a youtube channel

    Returns:
        bool: if titles of a channel are downloaded
    """
    channel = get(url)
    return channel['titles']


def get_playback(url: str) -> bool:
    """Checks if the playback data of a channel are already downloaded

    Args:
        url (str): link to a youtube channel

    Returns:
        bool: if playback data of a channel are downloaded
    """
    channel = get(url)
    return channel['playback']


def set_titles(url: str, b: bool) -> None:
    """Sets titles value for a certain link

    Args:
        url (str): link to a youtube channel
        b (bool): value titles will become
    """
    cache = read() 
    for channel in cache['channels']:
        if channel['url'] == url:
            channel['titles'] = b
    write(cache)
    

def set_playback(url: str, b: bool) -> None:
    """Sets playback value for a certain link

    Args:
        url (str): link to a youtube channel
        b (bool): value playback will become
    """
    cache = read()
    for channel in cache['channels']:
        if channel['url'] == url:
            channel['playback'] = b
    write(cache)


''' Testing '''
if __name__ == '__main__':
    read()
    test_url = 'https://null.null/test'
    for i in range(10):
        add("none", f"tester_{i}", f"{test_url}_{i}")
    
    if check(f"{test_url}_1"):
        print(f"{get_path(f'{test_url}_1')=}")
        print(f"{get_titles(f'{test_url}_1')=}")
        print(f"{get_playback(f'{test_url}_1')=}")
    try:
        print(get_path("invalid path"))
    except KeyError:
        ...
    try:
        print(get_titles("invalid path"))
    except KeyError:
        ...
    try:
        print(get_playback("invalid path"))
    except KeyError:
        ...
    
__all__ = ['check', 'add', 'get_path', 'get_titles', 'get_playback', 'set_titles', 'set_playback']
