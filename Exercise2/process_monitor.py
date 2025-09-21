import psutil
import time
import logging
from typing import List

logging.basicConfig(
    filename = "process_monitor.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"

)

class ProcessMonitor:
    def __init__(self,
                 processes:List[str],
                 poll_interval: int = 5,
                 cpu_threshold: int = 80,
                 mem_threshold: int = 80,
                 disk_threshold: int = 80,):
        """
        :param processes: list of process names to monitor
        :param poll_interval: seconds between checks
        :param cpu_threshold: CPU usage % threshold
        :param mem_threshold: Memory usage % threshold
        :param disk_threshold: Disk usage % threshold

        """
        self.processes = processes
        self.poll_interval = poll_interval
        self.thresholds = {
            "CPU": cpu_threshold,
            "Memory": mem_threshold,
            "Disk": disk_threshold
        }
    
    def is_process_running(self,process_name:str) -> bool:
        """Check if a process with the given name is running."""
        for proc in psutil.process_iter(attrs=["name"]):
            try:
                if process_name.lower() in proc.info["name"].lower():
                    return True
            except(psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return False
    
    def check_system_usage(self):
        """ Return CPU,Memory, and disk usage as a dict"""
        return{
        "CPU" : psutil.cpu_percent(interval=1),
        "Memory" : psutil.virtual_memory().percent,
        "Disk" : psutil.disk_usage("/").percent,
        }
        

        
    def monitor(self,duration: int = 30):
        """Monitor processes and system resources for a given duration (seconds)."""
        logging.info("Starting process and resource monitoring")

        start_time = time.time()
        while time.time() - start_time < duration:
            #Check processes
            for process in self.processes:
                if not self.is_process_running(process):
                    logging.warning(f"Process {process} is not running")
            # Check resources
            stats = self.check_system_usage()
            for resource, value in stats.items():
                if resource not in self.thresholds:
                    logging.error(f"No threshold defined for {resource}, skipping check")
                    continue
                threshold = self.thresholds[resource]
                if value > threshold:
                    logging.warning(f"High {resource} usage detected: {value}% ( threshold {threshold}%)")
            time.sleep(self.poll_interval)
        logging.info("Monitoring finished")


if __name__ == "__main__":
    monitor = ProcessMonitor(processes = ['python','sshd'])
    monitor.monitor(duration=20)