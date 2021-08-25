# msprites, media thumbnail sprites, multiple thumbnail sprites

# Requirements:

    1. FFmpeg
    2. ImageMagick Montage

# Steps:
    1. Extract images using ffmpeg. You can configure size of image and image rate per second(ips)
    2. Convert Image in spirtesheet of grid ROWSxCOLS
    3. Create a vtt file of spritesheet images that's compatible with Plyr.io

It uses temp folder for storage. for persistence storage move these different folder or location.
* It is not recommended to change the IPS value as anything besides 1 generates incorrect vtt data.

# Example Usage:
```
import os
from msprites import Settings as SpriteSetting
from msprites import MontageSprites

SpriteSetting.load(width=150, height=150)
sprite = MontageSprites.from_media(
    path="myvideo.mp4", create_webvtt=True, copy_dest=""
)

print(sprite.dir.name)
for filename in os.listdir(sprite.dir.name):
    print(filename)
```


