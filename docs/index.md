# Getting Started

[![license][badge]][license]

**AvalonYoutubeAgent.bundle** is a metadata agent for Plex.

## Requirements

* Plex
* [youtube-dl][youtube-dl]
* [Google API Key (Optional)][api]

## Install 

```bash
cd /var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-ins/
git clone https://github.com/joshuaavalon/AvalonYoutubeAgent.bundle.git
chown plex:plex AvalonYoutubeAgent.bundle
service plexmediaserver restart
```

Or copy the files to your `<Plex>/Plug-ins/AvalonYoutubeAgent.bundle`.

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

[schema]: https://joshuaavalon.github.io/AvalonYoutubeAgent.bundle/
[api]: https://developers.google.com/youtube/v3/getting-started
[license]: https://github.com/joshuaavalon/AvalonYoutubeAgent.bundle/blob/master/LICENSE
[badge]: https://img.shields.io/github/license/joshuaavalon/AvalonYoutubeAgent.bundle.svg
[youtube-dl]: https://github.com/rg3/youtube-dl
[agent]: https://github.com/ZeroQI/YouTube-Agent.bundle
