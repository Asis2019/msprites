import os
import shutil
import tempfile

from msprites import FFmpegThumbnails
from msprites.command import Command
from msprites.constants import THUMBNAIL_SPRITESHEET
from msprites.settings import Settings
from msprites.webvtt import WebVTT


class MontageSprites(Settings):

    def __init__(self, thumbs):
        self.thumbs: FFmpegThumbnails = thumbs
        self.dir = tempfile.TemporaryDirectory()

    def dest(self):
        return os.path.join(self.dir.name, self.FILENAME_FORMAT.format(ext=self.EXT))

    def generate(self):
        cmd = THUMBNAIL_SPRITESHEET.format(
            rows=self.ROWS,
            cols=self.COLS,
            width=self.WIDTH,
            height=self.HEIGHT,
            input=self.thumbs.dir.name,
            output=self.dest()
        )
        Command.execute(cmd)

    def cleanup(self):
        try:
            self.dir.cleanup()
            self.thumbs.cleanup()
        except OSError:
            pass

    def count(self):
        return len(os.listdir(self.dir.name))

    def to_webvtt(self, create_webvtt):
        if not create_webvtt:
            return
        webvtt = WebVTT(self)
        webvtt.generate()

    def copy_to(self, copy_dest):
        for file_name in os.listdir(self.dir.name):
            source = self.dir.name + "/" + file_name
            destination = copy_dest + "/" + file_name
            if os.path.isfile(source):
                shutil.copy(source, destination)

    @classmethod
    def from_media(cls, path, create_webvtt=True, copy_dest=None):
        sprites = MontageSprites(FFmpegThumbnails.from_media(path))
        sprites.generate()
        sprites.to_webvtt(create_webvtt)
        if copy_dest:
            sprites.copy_to(copy_dest)
            sprites.cleanup()
        return sprites
