#!/usr/bin/python3
"""
Module for Log Parsing.
"""
import sys
import signal


def print_stats(total_size, status_counts):
    """
    Print the total file size and count of each status code.

    Args:
        total_size (int): The total size of all files.
        status_counts (dict): A dictionary
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def signal_handler(sig, frame):
    """
    Handle the keyboard interrupt signal to exit.
    """
    print_stats(total_size, status)
    sys.exit(0)


# Initialize global variables
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
            # Extract status code and file size
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in status:
                status[status_code] += 1
        except ValueError:
            continue

        # Count lines and print stats every 10 lines
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status)

    # Ensure stats are printed after the last line (if not a multiple of 10)
    if line_count % 10 != 0:
        print_stats(total_size, status)

except KeyboardInterrupt:
    # Handle manual interruption gracefully
    print_stats(total_size, status)
    raise
