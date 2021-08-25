import os
import time

from msprites.settings import Settings


class WebVTT:
    HEADER = "WEBVTT\n\n"
    TIME_FORMAT = "%H:%M:%S.000"
    TIMELINE_FORMAT = "{start} --> {end}\n"
    IMAGE_TITLE_FORMAT = "{filename}#xywh={x},{y},{w},{h}\n\n"
    FILENAME = "sprite.vtt"

    def __init__(self, sprites):
        self.sprites = sprites
        self.dir = sprites.dir

    @staticmethod
    def ips_seconds_to_timestamp(ips):
        return time.strftime(WebVTT.TIME_FORMAT, time.gmtime(ips))

    @staticmethod
    def get_position(img_number, w, h):
        # coordinate in sprite image for a given image
        grid_size = Settings.ROWS * Settings.COLS
        img_number = img_number - ((img_number // grid_size) * grid_size)
        x = img_number // Settings.ROWS * w
        y = img_number % Settings.COLS * h
        return x, y

    def content(self):
        contents = [WebVTT.HEADER]
        start, end, filename = 0, Settings.IPS, ""
        w, h, grid_size = Settings.WIDTH, Settings.HEIGHT, Settings.ROWS * Settings.COLS
        for i in range(0, self.sprites.thumbs.count()):
            filename = Settings.sprite_filename((i + 1) // grid_size)
            contents += [
                str(i + 1) + "\n",
                WebVTT.TIMELINE_FORMAT.format(
                    start=self.ips_seconds_to_timestamp(start),
                    end=self.ips_seconds_to_timestamp(end),
                ),
                WebVTT.IMAGE_TITLE_FORMAT.format(
                    x=self.get_position(i, w, h)[0],
                    y=self.get_position(i, w, h)[1],
                    w=w, h=h, filename=filename,
                )
            ]
            start = end
            end += Settings.IPS
        return contents

    def dest(self):
        return os.path.join(self.dir.name, Settings.PREFIX + self.FILENAME)

    def generate(self):
        with open(self.dest(), "w") as f:
            f.writelines(self.content())
