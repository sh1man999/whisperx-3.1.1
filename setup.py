import os
import platform

from setuptools import find_packages, setup


def read_requirements(path):
    with open(path) as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.strip().startswith("#")
        ]


setup(
    name="whisperx",
    py_modules=["whisperx"],
    version="3.1.1",
    description="Time-Accurate Automatic Speech Recognition using Whisper.",
    readme="README.md",
    python_requires=">=3.8",
    author="Max Bain",
    url="https://github.com/m-bain/whisperx",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=read_requirements(
        os.path.join(os.path.dirname(__file__), "requirements.txt")
    )
    + [f"pyannote.audio==3.1.1"],
    entry_points={
        "console_scripts": ["whisperx=whisperx.transcribe:cli"],
    },
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)
