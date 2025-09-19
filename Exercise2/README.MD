Exercise 2: Process & Resource Monitor (Intermediate)

Problem Statement:
Build a Python script that monitors system processes and generates an alert if a critical process (say "nginx") is not running or if CPU usage crosses 80%.

Requirements:

Poll every 10 seconds.

Check if "nginx" (or any process from a config file) is running.

If not → log alert + attempt restart (simulate with subprocess).

Collect CPU/Memory usage → save in CSV for later analysis.

Hints / Key Modules:

psutil, subprocess, time, csv

Follow-up (Interview Twist):

Add email/Slack notification when alert triggers.

Introduce retry with exponential backoff before restart.