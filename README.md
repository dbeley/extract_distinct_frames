# extract_distinct_frames

This script allows the extraction of the distinct frames/images from a video file or a youtube url (with the help of youtube-dl).

The script creates a folder and a pdf file, both containing all the distinct images found.

## Prerequisites

- img2pdf
- tqdm
- PIL
- youtube-dl
- ffmpeg

## Installation

```
pipenv install '-e .'
```

## Usage

```
pipenv run extract_distinct_frames -u URL
```

## Help

```
pipenv run extract_distinct_frames -h
```
