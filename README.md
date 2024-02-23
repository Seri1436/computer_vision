# opencv-computer-vision

Welcome to this course on OpenCV with Python.

## Prerequirement install

    brew install ffmpeg

    brew install bar
    brew install zbar

    brew install imagemagick
    brew install tesseract
    brew install tesseract-lang
    tesseract --list-langs

    which tesseract
    --> /opt/homebrew/bin/tesseract

## Install

    python -m venv .venv && source .venv/bin/activate

    pip install -r requirements.txt

## Reference

- [OpenCV tutorial for beginners](https://www.youtube.com/watch?v=eDIj5LuIL4A)

- [OpenCV Python Tutorials for Beginners 2020](https://www.youtube.com/playlist?list=PLMoSUbG1Q_r_sc0x7ndCsqdIkL7dwrmNF)
    
- [Object Detection 101 Course](https://www.youtube.com/watch?v=WgPbbWmnXJ8)

## projects

The code for the 2 projects we cover in this course is in a different repository.

Repositories:

- [Color detection](https://github.com/computervisioneng/color-detection-opencv) : [youtube](https://www.youtube.com/watch?v=aFNDh5k3SjU)

- [Face anonymizer](https://github.com/computervisioneng/face-anonymizer-ptyhon) : [youtube](https://www.youtube.com/watch?v=DRMBqhrfxXg)


- [OpenCV-Python-Tutorials-and-Projects](https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects?tab=readme-ov-file)

- [reference](https://geunuk.tistory.com/476)
- [reference](https://www.clien.net/service/board/park/17991925)
- [reference](https://syerco0.com/37)
- [reference](https://kig2929kig.github.io/python/yt-dlp/)

## Issue

### Case.1

    pip show youtube-dl

    vi ./.venv/lib/python3.11/site-packages/youtube_dl/extractor/youtube.py

    [ASIS]
    1794 : 'uploader_id': self._search_regex(r'/(?:channel|user)/([^/?&#]+)', owner_profile_url, 'uploader id') if owner_profile_url else None,
    
    [TOBE]
    1794 : 'uploader_id': self._search_regex(r'/(?:channel|user)/([^/?&#]+)', owner_profile_url, 'uploader id', fatal=False) if owner_profile_url else None,


    vi ./.venv/lib/python3.11/site-packages/pafy/backend_youtube_dl.py

    [ASIS]
    53 self._likes = self._ydl_info['like_count']
    54 self._dislikes = self._ydl_info['dislike_count']

    [TOBE]
    53 self._likes = self._ydl_info.get('like_count',0)
    54 self._dislikes = self._ydl_info.get('dislike_count',0)


### Case.2 (MacBook M1):raise ImportError('Unable to find zbar shared library')

mkdir ~/lib
ln -s $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib

https://stackoverflow.com/questions/71984213/macbook-m1raise-importerrorunable-to-find-zbar-shared-library-importerror


### Case.3 Install tesseract on MacOS

brew install imagemagick
brew install tesseract
brew install tesseract-lang
tesseract --list-langs

which tesseract
--> /opt/homebrew/bin/tesseract


### Case.4 Install QRCode on MacOS

brew install bar
brew install zbar