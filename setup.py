import setuptools
import extract_distinct_frames

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="extract_distinct_frames",
        version=extract_distinct_frames.__version__,
        author="dbeley",
        author_email="dbeley@protonmail.com",
        description="Extract distinct images in a video file or a youtube video",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/dbeley/extract_distinct_frames",
        packages=setuptools.find_packages(),
        entry_points={
            "console_scripts": [
                "extract_distinct_frames=extract_distinct_frames.__main__:main"
                ]
            },
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: POSIX :: Linux"
            ],
        install_requires=[
            'tqdm',
            'Pillow',
            ]
        )
