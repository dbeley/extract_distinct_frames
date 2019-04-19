import os
import logging

logger = logging.getLogger(__name__)


def extracting_images(file, directory):
    logger.info(f"Extracting images from {file} to {directory}")
    os.system(f"ffmpeg -i \"{file}\" -vf fps=0.25 \"{directory}/thumb%04d.jpg\" -hide_banner >/dev/null 2>&1")
