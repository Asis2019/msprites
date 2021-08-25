class Settings:
    IPS = 1  # default IPS value, 1 image per second
    WIDTH = 128
    HEIGHT = 72
    EXT = ".jpeg"
    ROWS = 30
    COLS = 30
    FILENAME_FORMAT = "%04d{ext}"
    PREFIX = ""

    @classmethod
    def load(cls, width=None, height=None, ips=None, ext=None, rows=None, cols=None, prefix=None):
        cls.IPS = ips or cls.IPS
        cls.EXT = ext or cls.EXT
        cls.ROWS = rows or cls.ROWS
        cls.COLS = cols or cls.COLS
        cls.WIDTH = width or cls.WIDTH
        cls.HEIGHT = height or cls.HEIGHT
        cls.PREFIX = prefix or cls.PREFIX

    @classmethod
    def sprite_filename(cls, number):
        name = cls.PREFIX + (cls.FILENAME_FORMAT % number)
        return name.format(ext=cls.EXT)
