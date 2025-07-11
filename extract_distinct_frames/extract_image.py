import logging
import subprocess

logger = logging.getLogger(__name__)


def extract_image(file, directory):
    logger.info("Extracting images from %s to %s", file, directory)
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            str(file),
            "-vf",
            "fps=0.25",
            f"{directory}/thumb%04d.jpg",
            "-hide_banner",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )
