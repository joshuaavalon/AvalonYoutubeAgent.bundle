# AvalonYoutubeAgent.bundle

[![license][badge]][license]

This is a Plex Youtube agent.

## Requirements

You need a Google API Key to access Youtube REST API.
You can read [this][api]

## Install 

```bash
cd /var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins/
git clone https://github.com/joshuaavalon/AvalonYoutubeAgent.bundle.git
chown plex:plex AvalonYoutubeAgent.bundle
service plexmediaserver restart
```

## How to use

First, you can use [youtube-dl][youtube-dl] to download the video. 
You need `--write-info-json` to get the metadata of the videos.
You are recommend to download the thumbnail with `--write-thumbnail` as well.

Then, you need to rename your file to Plex naming scheme.

```
Channel/
├── Season 01/
│   ├── Channel - s01e01.mp4
│   ├── Channel - s01e01.jpg
│   └── Channel - s01e01.json
└── show.json
```

For `show.json`, you need to get it from `https://www.googleapis.com/youtube/v3/channels?part=brandingSettings,contentDetails&forUsername=<Uploader Id>&key=<API key>`

* `Uploader Id` is present in the video json as `uploader_id`
* `API key` can be create in Google API console.

Lastly, do not forget to choose `Avalon Youtube Agent` as agent.


## Frequently Asked Questions

**How is it different from [ZeroQI/YouTube-Agent.bundle][agent]?**

ZeroQI/YouTube-Agent.bundle relies on Youtube REST API. 
This means you can refresh metadata to get the latest metadata.
However, if Youtube is down or video is deleted, the metadata is no longer accessible which defeats the purpose of you archiving it.

## Customize metadata

You can customize metadata by editing the JSON. Youtube does not provide all the fields to fill in Plex.

### show.json

These fields to referring to `items > item[kind=youtube#channel] > brandingSettings > channel`.

| Plex                    | Youtube        | Type                       | Provided |
|-------------------------|----------------|----------------------------|----------|
| Title                   | title          | String                     | Y        |
| Sort Title              | title          | String                     | Y        |
| Content Rating          | content_rating | String                     | N        |
| Studio                  | studio         | String                     | N        |
| Originally Available At | aired          | String (`YYYYMMDD`)        | N        |
| Summary                 | description    | String                     | Y        |
| Rating                  | rating         | Float (0 ~ 10)             | N        |
| Genres                  | keywords       | String (Split by space)    | Y        |
| Collections             | collections    | List of string             | N        |
| Actors                  | actors         | Object (name, role, photo) | N        |

Note that `actors` is a JSON object and `photo` is the url of the image (Not path).

### episode

These fields to referring to root level of the JSON.

| Plex                    | Youtube        | Type                | Provided |
|-------------------------|----------------|---------------------|----------|
| Title                   | title          | String              | Y        |
| Originally Available At | upload_date    | String (`YYYYMMDD`) | Y        |
| Summary                 | description    | String              | Y        |
| Rating                  | average_rating | Float (0 ~ 10) * 2  | Y        |
| Writers                 | writers        | List of string      | N        |
| Directors               | directors      | List of string      | N        |

[schema]: https://joshuaavalon.github.io/AvalonYoutubeAgent.bundle/
[api]: https://developers.google.com/youtube/v3/getting-started
[license]: https://github.com/joshuaavalon/AvalonYoutubeAgent.bundle/blob/master/LICENSE
[badge]: https://img.shields.io/github/license/joshuaavalon/AvalonYoutubeAgent.bundle.svg
[youtube-dl]: https://github.com/rg3/youtube-dl
[agent]: https://github.com/ZeroQI/YouTube-Agent.bundle
