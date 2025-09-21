import pytest
from process_monitor import ProcessMonitor

@pytest.fixture
def monitor():
    # Monitor for "python" process(Pytest default runs python)
    return ProcessMonitor(['python'],poll_interval=1,cpu_threshold=90,mem_threshold=90,disk_threshold=95)

def test_is_process_running(monitor):
    assert monitor.is_process_running("python") is True

def test_is_process_not_running(monitor):
    assert monitor.is_process_running("dummy") is False

def test_check_system_usage(monitor):
    stats = monitor.check_system_usage()
    assert "CPU" in stats
    assert "Memory" in stats
    assert "Disk" in stats
    assert 0 <= stats['CPU'] <= 100
    assert 0 <= stats['Memory'] <= 100
    assert 0 <= stats['Disk'] <= 100

def test_thresholds_are_configurable():
    m = ProcessMonitor(["python"],cpu_threshold=50,mem_threshold=60,disk_threshold=70)
    assert m.thresholds["CPU"] == 50
    assert m.thresholds["Memory"] == 60
    assert m.thresholds["Disk"] == 70

def test_missing_threshold_logs_error(caplog):
    class DummyMonitor(ProcessMonitor):
        def check_system_usage(self):
            return { "CustomResource": 42} # resource not in thresholds
    m = DummyMonitor(["python"])
    with caplog.at_level("ERROR"):
        m.monitor(duration=1)
    assert "No threshold defined for CustomResource" in caplog.text

def test_monitor_runs_without_crash(monitor,caplog):
    with caplog.at_level("INFO"):
        monitor.monitor(duration=2)
    assert "Monitoring finished" in caplog.text

def test_high_usage_triggers_warnings(caplog):
    class DummyMonitor(ProcessMonitor):
        def check_system_usage(self):
            return {
                "CPU":95,
                "Memory":96,
                "Disk":97,
            }
    m = DummyMonitor(["python"], cpu_threshold=80,mem_threshold=80,disk_threshold=80)
    with caplog.at_level("WARNING"):
        m.monitor(duration=1)

    assert "High CPU usage detected" in caplog.text
    assert "High Memory usage detected" in caplog.text
    assert "High Disk usage detected" in caplog.text

def test_missing_process_logs_warning(caplog):
    m = ProcessMonitor(["Dummy"],poll_interval=1)
    with caplog.at_level("WARNING"):
        m.monitor(duration=1)
    print("\n--- caplog.text ---")
    print(caplog.text)
    
    assert "Process Dummy is not running" in caplog.text