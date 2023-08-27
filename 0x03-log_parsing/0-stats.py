#!/usr/bin/python3

"""
Log Parsing and Metrics Computation
"""

import sys
import signal

# Signal handler to print statistics on Ctrl+C
def handle_interrupt(signal, frame):
    print_statistics()

# Register Ctrl+C signal handler
signal.signal(signal.SIGINT, handle_interrupt)

def print_statistics():
    total_size = sum(file_sizes)
    print("File size: {}".format(total_size))
    
    for status_code in sorted(status_codes.keys()):
        print("{}: {}".format(status_code, status_codes[status_code]))

# Initialize variables to store statistics
file_sizes = []
status_codes = {}

try:
    # Process each line from stdin
    for line_number, line in enumerate(sys.stdin, start=1):
        parts = line.split()
        if len(parts) >= 7:
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                file_sizes.append(file_size)
                
                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1
                
                # Print statistics after every 10 lines
                if line_number % 10 == 0:
                    print_statistics()

            except ValueError:
                pass

except KeyboardInterrupt:
    # Handle Ctrl+C interruption by printing statistics
    print_statistics()
    sys.exit(0)
