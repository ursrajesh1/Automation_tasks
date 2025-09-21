# Exercise 1: File System Monitor

## 📌 Overview
This exercise implements a **file system monitor** in Python that tracks:
- File creation, deletion, and modification events.
- Ignores `.log` files to prevent self-monitoring.
- Logs all detected changes to a file.

This is the foundation of system-level monitoring, later extended in Exercise 2.

---

## 📌 Features
- Monitors a target directory for:
  - **Created files**
  - **Deleted files**
  - **Modified files**
- Ignores files with `.log` extension.
- Configurable polling interval and monitoring duration.
- Logs events with timestamps.

---

## 📌 Files
- `file_monitor.py` → Main implementation (`FileSystemMonitor` class).  
- `test_file_monitor.py` → Unit tests using `pytest`.  
- `file_monitor.log` → Log file generated at runtime (ignored in git).  

---

## 📌 How to Run
```bash
python file_monitor.py

## 📌 How to Test
pytest -v Exercise1/test_file_monitor.py
