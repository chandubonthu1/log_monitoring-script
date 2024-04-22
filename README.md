# log_monitoring-script
# Log Monitoring and Analysis Script

This script continuously monitors a specified log file for new entries and performs basic analysis on the log entries.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Introduction

The Log Monitoring and Analysis Script is a Python script designed to monitor a specified log file in real-time and perform basic analysis on the log entries. It tracks new log entries as they are added to the file, analyzes them to detect specific patterns or keywords, and generates summary reports based on the analysis.

## Usage

1. Clone the repository:

    ```bash
    git clone <repository_link>
    cd log-monitoring-script
    ```

2. Make sure you have Python 3 installed on your system.

3. Modify the `LOG_FILE` variable in `log_monitor.py` to specify the path to the log file you want to monitor.

4. Run the script:

    ```bash
    python3 log_monitor.py
    ```

5. To stop the monitoring, press Ctrl+C.

## Dependencies

- Python 3


