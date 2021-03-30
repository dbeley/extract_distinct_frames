import argparse
import logging
import time
import os
import img2pdf
from pathlib import Path
from tqdm import tqdm
from .compare_images import compare_images
from .downloading_video import downloading_video
from .extracting_images import extracting_images

logger = logging.getLogger()
temps_debut = time.time()


def main():
    args = parse_args()
    # Downloading video
    if not args.file:
        if not args.url:
            logger.error(
                "No video file or url entered. Use the -h argument to see available options"
            )
            exit()
        else:
            logger.info("Downloading %s", args.url)
            video_filename = downloading_video(args.url)
            logger.info("Finished downloading %s", video_filename)
        video_file = Path(video_filename)
    else:
        video_file = Path(args.file)
    filename = Path(video_file).stem

    export_directory = f"{filename}_images"
    Path(export_directory).mkdir(parents=True, exist_ok=True)

    logger.debug("Extracting images to %s", export_directory)
    extracting_images(video_file, export_directory)

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
            score = compare_images(old, file)
            # Threshold = 2
            if score < 2:
                Path.unlink(file)
            else:
                old = file

    logger.info("Suppressing %s", video_file)
    os.remove(video_file)

    # Create pdf file with remaining images
    pathlist = Path(export_directory).glob("**/*.jpg")
    images = [str(x) for x in sorted(pathlist)]

    logger.info("Creating pdf file")
    with open(f"{filename}.pdf", "wb") as f:
        f.write(img2pdf.convert(images))

    print("Runtime : %.2f seconds" % (time.time() - temps_debut))


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
