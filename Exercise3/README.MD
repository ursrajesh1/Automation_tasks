Exercise 3: Configuration Drift Detector (Advanced)

Problem Statement:
Create a Python tool that compares two system configuration snapshots (JSON/YAML) and highlights differences.

Requirements:

Take two JSON config files as input.

Compare key-value pairs recursively (nested dicts).

Output differences in a structured format:

Changed: key1 → old: X, new: Y  
Added: key2 → value: Z  
Removed: key3 → old: W  


Save report to a file.

Hints / Key Modules:

json, difflib, deepdiff (optional for advanced).

Follow-up (Interview Twist):

Integrate with Git to show drift from last committed version.

Run as part of CI/CD pipeline for infra validation.