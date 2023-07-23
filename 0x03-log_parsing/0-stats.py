#!/usr/bin/env python3
"""
Script to read log input from standard in line by line
and compute metrics
"""
import sys


def print_stats(stats):
    """
    Outputs log statistics after every 10 lines or on keyboard
    interrupt

    Args:
        stats (dict): dictionary of key value pairs

    Return:
        Output stats
    """
    total_size = sum(stats.values())
    print(f"File size: {total_size}")

    sorted_codes = sorted(stats.keys())
    for code in sorted_codes:
        print("{:d}: {:d}".format(code, stats[code]))


def main():
    """
    Function to parse log line by line and extract status code and file size
    info

    Args:
        None

    Returns:
        None
    """
    stats = {}
    line_count = 0
    try:
        for line in sys.stdin:
            line_count += 1

            if line_count % 10 == 0:
                print_stats(stats)

            try:
                parts = line.strip().split()
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    stats[status_code] = stats.get(status_code, 0) + 1

            except (IndexError, ValueError):
                pass

    except KeyboardInterrupt:
        print("Keyboard interruption detected.")
    finally:
        print_stats(stats)


if __name__ == "__main__":
    main()
