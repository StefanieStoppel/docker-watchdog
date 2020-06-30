import os
import time

from PIL import Image
from PIL.ImageOps import grayscale
from watchdog.events import RegexMatchingEventHandler


class ImageEventHandler(RegexMatchingEventHandler):
    IMAGE_REGEX = [r".*(-color)\.png$"]

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
        filename = f"{filename.replace('color', 'grayscale')}.png"

        image = Image.open(event.src_path)
        image = grayscale(image)
        image.save(filename)
