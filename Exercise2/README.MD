# Exercise 2: Process & Resource Monitor

## 📌 Overview
This exercise implements a **system-level monitor** in Python that tracks:
- Whether specified processes are running.
- CPU, Memory, and Disk usage.
- Logs warnings when thresholds are exceeded.

It extends the first exercise by monitoring not just the file system, but also system processes and resources.

---

## 📌 Features
- Detects if a given process (e.g., `python`, `sshd`) is running.
- Tracks system usage:
  - CPU %
  - Memory %
  - Disk usage %
- Configurable thresholds (default: 80%).
- Logs alerts when resources exceed thresholds.
- Ignores unconfigured resources with an error log.

---

## 📌 Files
- `process_monitor.py` → Main implementation.
- `test_process_monitor.py` → Unit tests using `pytest`.
- `process_monitor.log` → Log file generated at runtime (ignored in git).

---

## 📌 How to Run
```bash
python process_monitor.py

## 📌 How to test
pytest -v Exercise2/test_process_monitor.py

📌 Sample Log Output
2025-09-19 17:00:01,234 - INFO - Starting process and resource monitoring
2025-09-19 17:00:06,245 - WARNING - Process sshd is not running
2025-09-19 17:00:06,246 - WARNING - High CPU usage detected: 92% (threshold 80%)
2025-09-19 17:00:21,345 - INFO - Monitoring finished

