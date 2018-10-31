from base64 import b64encode
from datetime import datetime


def create_id(title, year):
    return b64encode("%s:%d" % (title, year)).replace("/", "_")


def set_metadata_list(metadata, field, source):
    metadata_list = getattr(metadata, field)
    if source is not None and metadata_list is not None:
        metadata_list.clear()
        for value in source:
            metadata_list.add(value)


def set_metadata_list_name(metadata, field, source):
    metadata_list = getattr(metadata, field)
    if source is not None and metadata_list is not None:
        metadata_list.clear()
        for value in source:
            metadata_list.new().name = value


def set_metadata_actors(metadata, actors):
    metadata.roles.clear()
    if actors is None:
        return
    for actor in actors:
        role = metadata.roles.new()
        role.name = actor.get("name")
        role.role = actor.get("role")
        role.photo = actor.get("photo")


def convert_date(date_str):
    if date_str is None:
        return None
    try:
        date = datetime.strptime(date_str, "%Y%m%d")
    except ValueError:
        return None
    return date


def join_list_or(items, sep=" / ", default=None):
    if items is None or len(items) <= 0:
        return default
    return sep.join(items)


def first_or(items, default=None):
    if items is None or len(items) <= 0:
        return default
    return items[0]
