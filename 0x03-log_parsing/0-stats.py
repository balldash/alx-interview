#!/usr/bin/python3
"""
Module for Log Parsing.
"""
import sys
import signal


def print_stats(total_size, status):
    """
    Print the total file size and count of each status code.

    Args:
        total_size (int): The total size of all files.
        status (dict): A dict with status codes as keys and their counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status.keys()):
        if status[code] > 0:
            print(f"{code}: {status[code]}")


def signal_handler(sig, frame):
    """
    Handle the keyboard interrupt signal (CTRL + C) to print statistics and
    exit.

    Args:
        sig (int): The signal number.
        frame (frame object): The current stack frame.
    """
    global total_size, status
    print_stats(total_size, status)
    sys.exit(0)


# Set up signal handler
signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in status:
                status[status_code] += 1
        except ValueError:
            continue
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status)
except KeyboardInterrupt:
    print_stats(total_size, status)
    raise
