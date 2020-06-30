import os
import time

from PIL import Image
from PIL.ImageOps import invert
from watchdog.events import RegexMatchingEventHandler


class ImageEventHandler(RegexMatchingEventHandler):
    IMAGE_REGEX = [r".*(\d{6})(-(color|depth))(_grayscale)\.png$"]

    def __init__(self):
        super().__init__(self.IMAGE_REGEX)

    def on_created(self, event):
        print(f"Processing {event.src_path}")
        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            file_size = os.path.getsize(event.src_path)
            time.sleep(1)
        self.process(event)

    def process(self, event):
        filename, ext = os.path.splitext(event.src_path)
        filename = f"{filename.replace('grayscale', 'invert')}.png"

        image = Image.open(event.src_path)
        image = invert(image)
        image.save(filename)
