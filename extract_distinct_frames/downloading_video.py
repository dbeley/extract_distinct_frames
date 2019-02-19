import os
import re
import logging

logger = logging.getLogger()


def downloading_video(file, url):
    logger.info(f"Downloading {url} to {file}")
    os.system(f"youtube-dl -f \'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4\' {re.escape(url)} --output {file}")
