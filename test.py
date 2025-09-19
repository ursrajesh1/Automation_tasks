import os
import time
import tempfile
import pytest
from file_monitor import FileSystemMonitor

@pytest.fixture
def temp_dir():
    """ Provide a temporary directory for eac test."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

@pytest.fixture
def monitor(temp_dir):
    """ Provide a FileSystemMonitor Instance for the temp dicretory."""
    return FileSystemMonitor(temp_dir,poll_interval=1)

def test_ignore_log_files(monitor,temp_dir):
    log_file = os.path.join(temp_dir, "debug.log")
    txt_file = os.path.join(temp_dir, "notes.txt")

    with open(log_file, "w") as f:
        f.write("Ignore me from the monitoring")
    with open(txt_file,'w') as f:
        f.write("Please monitor the change to this file")
    
    snap = monitor.snapshot()
    assert txt_file in snap
    assert log_file not in snap

def test_added_file_detection(monitor,temp_dir):
    snap1 = monitor.snapshot()
    new_file =os.path.join(temp_dir,"file1.txt")
    with open(new_file,"w") as f:
        f.write("Hello")
    
    snap2  = monitor.snapshot()
    added,removed,modified = monitor.detect_changes(snap1,snap2)

    assert new_file in added
    assert not removed
    assert not modified

def test_modified_file_detection(monitor,temp_dir):
    """ Create a new file instead of using file created in test_added """
    file_path = os.path.join(temp_dir,"file_modified.txt")
    with open(file_path,"w") as f:
        f.write("original")
    
    snap1 = monitor.snapshot()

    # modify the file
    time.sleep(2)
    with open(file_path,"a") as f:
        f.write("updated")
    
    snap2 = monitor.snapshot()

    added,removed,modified = monitor.detect_changes(snap1,snap2)

    assert file_path in modified
    assert not added
    assert not removed
def test_deleted_file_detection(monitor,temp_dir):
    """Using files created in the added  TCs"""
    del_file =os.path.join(temp_dir,"file1.txt")
    with open(del_file,"w") as f:
        f.write("temp")
    
    snap1 = monitor.snapshot()

    os.remove(del_file)
    time.sleep(2)
    snap2 = monitor.snapshot()
    added,removed,modified = monitor.detect_changes(snap1,snap2)

    assert del_file in removed
    assert not added
    assert not modified






