# Automation Tasks

This repository contains system-level automation exercises in Python.  
Each exercise focuses on a different area of automation that an SDET / Systems Test Engineer might encounter in real-world scenarios.

---

## 📌 Exercises

### [Exercise1](Exercise1)
**File System Monitor**  
- Monitors a directory for file changes (create, modify, delete).  
- Ignores `.log` files to prevent self-tracking.  
- Includes unit tests with `pytest`.  

---

### [Exercise2](Exercise2)
**Process & Resource Monitor**  
- Monitor system processes (e.g., check if critical process is running).  
- Track CPU and memory usage.  
- Log results and alert if thresholds are exceeded.  

---

### [Exercise3](Exercise3)
**Configuration Drift Detector**  
- Compare two configuration snapshots (JSON/YAML).  
- Report added, removed, and modified keys.  
- Useful for detecting system config mismatches.  

---

## 📌 How to Run Tests
From inside each exercise folder, run:
```bash
pytest -v


📌 Requirements

Python 3.9+

pytest

📌 Author

Rajesh Kandula
System & Scale Testing | Automation | Python