import logging
from youtube_dl import YoutubeDL

logger = logging.getLogger(__name__)


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def downloading_video(url):
    ydl_opts = {
            # 'quiet': True,
            'logger': MyLogger(),
    }
    with YoutubeDL(ydl_opts) as ydl:
        logger.debug("Downloading video at %s", url) 
        info_dict = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info_dict)
    return filename
