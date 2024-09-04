import os
import time

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

source_dir = "/Users/mickeyarnold/Downloads"
image_folder = "/Users/mickeyarnold/Desktop/100daysofpython/images_folder"

image_files = [".jpg", ".jpeg", ".png", ".gif", ".bmp",".HEIC"]



class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event: FileSystemEvent) -> None:
        # files in download folder
        allfiles = os.listdir(source_dir)
        count = 0
        for files in allfiles:
            # check if I was grabbing the files
            # print(type(files))
            if files.endswith(tuple(image_files)):
                count+=1
                src_path = os.path.join(source_dir, files)
                dst_path = os.path.join(image_folder,files)
                os.rename(src_path, dst_path)

        # print(event)


event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler,source_dir, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()