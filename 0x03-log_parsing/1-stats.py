#!/usr/bin/python3
"""
Script to read log input from standard in line by line
and compute metrics
"""
import signal
import sys

stats = {}
total_size = 0
line_count = 0


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
    print("File size: {}".format(total_size))

    sorted_codes = sorted(stats.keys())
    for code in sorted_codes:
        print("{:d}: {:d}".format(code, stats[code]))


def signal_handler(sig, frame):
    """
    Handle Keyboard Interrupt (SIGINT).

    Args:
        sig (int): The signal number.
        frame (frame): The current stack frame

    Returns:
        None
    """
    print_stats(stats, total_size)
    sys.exit(0)


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
    total_size = 0
    line_count = 0

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            try:
                parts = line.strip().split()
                status_code = int(parts[-2])
                file_size = int(parts[7])

                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    stats[status_code] = stats.get(status_code, 0) + 1

                total_size += file_size

            except (IndexError, ValueError):
                pass
            line_count += 1

            if (line_count != 0) and (line_count % 10 == 0):
                print_stats(stats)


    except KeyboardInterrupt:
        """Keyboard interrupt: print from beginning"""
        print_stats(stats)
        raise


if __name__ == "__main__":
    main()
