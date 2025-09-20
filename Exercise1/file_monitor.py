import os
import time
import logging
from typing import Dict

logging.basicConfig(
    filename = "file_monitor.log",
    level = logging.INFO,
    format = "%(asctime)s - %(message)s",

)

class FileSystemMonitor:

    def __init__(self,directory:str,poll_interval: int = 5):
        self.directory = directory
        self.poll_interval = poll_interval
        self.previous_snapshot : Dict[str, float] = {}
    
    def snapshot(self) -> Dict[str, float]:
        files = {}
        for root, _ ,filenames in os.walk(self.directory):
            for fname in filenames:
                fpath = os.path.join(root,fname)
                if fpath.endswith(".log"):
                    continue

                try:
                    files[fpath] = os.path.getmtime(fpath)
                except FileNotFoundError:
                    continue
        return files
    def detect_changes(self,old_snap:Dict[str,float],new_snap:Dict[str,float]):
        """Detect added,removed,modified files"""

        old_files, new_files = set(old_snap.keys()), set(new_snap.keys())

        added_files = new_files - old_files
        removed_files = old_files - new_files
        modified_files = {f for f in old_files & new_files if old_snap[f] != new_snap[f]}

        return added_files, removed_files,modified_files
    def monitor(self, duration: int =30):
        """ Monitor directory for a given duration """
        logging.info(f"Starting monitor on {self.directory}")
        self.previous_snapshot = self.snapshot()
        start_time = time.time()

        while time.time() - start_time < duration:
            time.sleep(self.poll_interval)
            current_snapshot = self.snapshot()
            added_files, removed_files,modified_files =self.detect_changes(
                self.previous_snapshot,current_snapshot)
            
            for f in added_files:
                logging.info(f"Created: {f}")
            for f in removed_files:
                logging.info(f"Deleted: {f}")
            for f in modified_files:
                logging.info(f"Modifed: {f}")
            
            self.previous_snapshot = current_snapshot
        logging.info("Monitoring finished")


if __name__ == "__main__":
    directory_name = "./Excersice1" #Provide actual path
    os.makedirs(directory_name,exist_ok=True)

    monitor_tasks = FileSystemMonitor(directory_name, poll_interval=2)

    monitor_tasks.monitor(duration=20)

