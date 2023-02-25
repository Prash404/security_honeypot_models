from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print("File modified:", event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            print("File created:", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            print("File deleted:", event.src_path)

observer = Observer()
observer.schedule(MyHandler(), path='D:\/vscode files\code files\/ransomware research')
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()

observer.join()
