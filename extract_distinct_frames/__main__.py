import argparse
import logging
import time
import os
import img2pdf
from pathlib import Path
from tqdm import tqdm
from .compare_image import compare_image
from .download_video import download_video
from .extract_image import extract_image

logger = logging.getLogger()
START_TIME = time.time()


def main():
    args = parse_args()
    # Downloading video
    if not args.file:
        if not args.url:
            raise Exception(
                "No video file or url entered. Use the -h argument to see available options"
            )
        else:
            logger.info("Downloading %s", args.url)
            video_filename = download_video(args.url)
            logger.info("Finished downloading %s", video_filename)
    else:
        video_filename = args.file
    filename = Path(video_filename).stem

    export_directory = f"{filename}_images"
    Path(export_directory).mkdir(parents=True, exist_ok=True)

    logger.debug("Extracting images to %s", export_directory)
    extract_image(video_filename, export_directory)

    # Compare images
    pathlist_size = sum(1 for x in Path(export_directory).glob("**/*.jpg"))
    pathlist = Path(export_directory).glob("**/*.jpg")
    first = True
    logger.info("Comparing images")
    for file in tqdm(sorted(pathlist), dynamic_ncols=True, total=pathlist_size):
        if first:
            old = file
            first = False
        else:
            score = compare_image(old, file)
            # Threshold = 2
            if score < 2:
                Path.unlink(file)
            else:
                old = file

    logger.info("Suppressing %s", video_filename)
    try:
        os.remove(video_filename)
    except Exception as e:
        logger.warning(f"Couldn't remove video file {video_filename}: {e}")

    # Create pdf file with remaining images
    pathlist = Path(export_directory).glob("**/*.jpg")
    images = [str(x) for x in sorted(pathlist)]

    logger.info("Creating pdf file")
    with open(f"{filename}.pdf", "wb") as f:
        f.write(img2pdf.convert(images))

    logger.info("Runtime : %.2f seconds" % (time.time() - START_TIME))


def parse_args():
    parser = argparse.ArgumentParser(description="Extract unique images from videos")
    parser.add_argument(
        "--debug",
        help="Display debugging information",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.INFO,
    )
    parser.add_argument("-f", "--file", help="Video file", type=str)
    parser.add_argument("-u", "--url", help="URL of the video", type=str)
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)
    return args


if __name__ == "__main__":
    main()
