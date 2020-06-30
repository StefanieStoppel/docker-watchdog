import os
import time

from watchdog.observers import Observer

from src.app1.image_event_handler import ImageEventHandler


class ImageWatcher:
    def __init__(self, src_path):
        self.__src_path = src_path
        self.__event_handler = ImageEventHandler()
        self.__event_observer = Observer()

    def run(self):
        print(f"Watching directory {self.__src_path}")
        self.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )


if __name__ == "__main__":
    input_dir = os.path.abspath(os.getenv("INPUT_DIR"))
    print(f"input_dir: {input_dir}")
    src_path = input_dir if input_dir is not None else '.'
    ImageWatcher(src_path).run()
