import os
import re
import logging

logger = logging.getLogger()


def extracting_images(file, directory):
    logger.info(f"Extracting images from {file} to {directory}")
    os.system(f"ffmpeg -i {re.escape(file)} -vf fps=0.25 {directory}/thumb%04d.jpg -hide_banner")
