Exercise 1: File System Monitor (Beginner → Intermediate)

Problem Statement:
Write a Python script that monitors a given directory and logs all file changes (created, modified, deleted).

Requirements:

Take directory path as input (from CLI args).

Detect:

New file creation

File modification (timestamp/size)

File deletion

Log events to a file with timestamp.

Hints / Key Modules:

os, time, hashlib, logging (basic polling)

For advanced version → use watchdog library (event-driven).

Follow-up (Interview Twist):

Extend script to copy new/modified files to a backup folder automatically.

How would you scale this if directory has millions of files?