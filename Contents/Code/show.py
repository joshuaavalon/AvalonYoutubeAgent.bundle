import hashlib
import re
from os.path import basename, dirname, exists, join, splitext
from urllib import unquote

from log import PlexLog
from utils import convert_date, set_metadata_actors, set_metadata_list

EPISODE_REGEX = "^(.*\S)\s+-\s+s\d{2,}e\d{2,}.*$"


def get_show_json(media):
    if hasattr(media, "filename"):
        path = unquote(media.filename).decode("utf8")
    else:
        path = get_show_file(media)
    season_dir = dirname(path)
    show_dir = dirname(season_dir)
    file_path = join(show_dir, "show.json")
    if not exists(file_path):
        return None
    string = Core.storage.load(file_path)
    show = JSON.ObjectFromString(string)
    return get_channel(show)


def get_channel(show):
    if "items" not in show:
        return None
    items = show.get("items", [])
    item = None
    for i in items:
        if i.get("kind") == "youtube#channel":
            item = i
            break
    if item is None:
        return None
    try:
        return item["brandingSettings"]["channel"]
    except KeyError:
        return None


def get_episode_json(media, season, episode):
    path = get_show_file(media)
    season_dir = dirname(path)
    name = guess_name(path)
    file = episode_file(name, season, episode, "json")
    file_path = join(season_dir, file)
    if not exists(file_path):
        PlexLog.error("No JSON for %s" % file_path)
        return None
    string = Core.storage.load(file_path)
    return JSON.ObjectFromString(string)


def set_show(metadata, channel):
    metadata.title = channel.get("title")
    metadata.title_sort = channel.get("title")
    metadata.original_title = channel.get("title")
    metadata.content_rating = channel.get("content_rating")
    metadata.studio = channel.get("studio")
    metadata.originally_available_at = convert_date(channel.get("aired"))
    metadata.summary = channel.get("description")
    metadata.rating = channel.get("rating")
    set_metadata_list(metadata, "genres", channel.get("keywords").split())
    set_metadata_list(metadata, "collections", channel.get("collections"))
    set_metadata_actors(metadata, channel.get("actors", []))


def get_show_file(media):
    if hasattr(media, "filename") and media.filename is not None:
        return unquote(media.filename).decode("utf8")
    for season in media.seasons:
        for episode in media.seasons[season].episodes:
            e = media.seasons[season].episodes[episode]
            return e.items[0].parts[0].file
    return None


def set_episode(metadata, episode):
    metadata.title = episode.get("title")
    metadata.content_rating = episode.get("content_rating")
    metadata.originally_available_at = convert_date(episode.get("upload_date"))
    metadata.summary = episode.get("description")
    metadata.rating = episode.get("average_rating") * 2
    set_metadata_list(metadata, "writers", episode.get("writers", []))
    set_metadata_list(metadata, "directors", episode.get("directors", []))


def set_episode_cover(metadata, media, season, episode):
    path = get_show_file(media)
    name = guess_name(path)
    season_dir = dirname(path)
    jpg = episode_file(name, season, episode, "jpg")
    file_path = join(season_dir, jpg)
    if not exists(file_path):
        png = episode_file(name, season, episode, "png")
        file_path = join(season_dir, png)
    if not exists(file_path):
        return
    cover = Core.storage.load(file_path)
    key = hashlib.md5(cover).hexdigest()
    metadata.thumbs[key] = Proxy.Media(cover)


def guess_name(path):
    file_name = basename(path)
    name, ext = splitext(file_name)
    result = re.search(EPISODE_REGEX, name)
    return result.group(1)


def episode_file(name, season, episode, ext):
    return "%s - s%se%s.%s" % (name, season.zfill(2), episode.zfill(2), ext)
