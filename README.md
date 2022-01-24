# extract_distinct_frames

This script allows the extraction of the distinct frames/images from a video file or a youtube url (with the help of youtube-dl).

The script creates a folder and a pdf file, both containing all the distinct images found.

## Prerequisites

- img2pdf
- tqdm
- pillow
- yt-dlp
- ffmpeg

## Installation in a virtualenv

```
pipenv install '-e .'
```

## Usage

```
extract_distinct_frames -u URL
```

## Help

```
extract_distinct_frames -h
```

```
usage: extract_distinct_frames [-h] [--debug] [-f FILE] [-u URL]

Extract unique images from videos

optional arguments:
  -h, --help            show this help message and exit
  --debug               Display debugging information
  -f FILE, --file FILE  Video file
  -u URL, --url URL     URL of the video
```
