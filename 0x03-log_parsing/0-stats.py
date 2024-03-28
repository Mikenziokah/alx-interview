#!/usr/bin/python3
import sys

# Define status codes
STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize variables
total_file_size = 0
status_counts = {code: 0 for code in STATUS_CODES}
line_count = 0

try:
    # Read stdin line by line
    for line in sys.stdin:
        # Split the line
        parts = line.split()
        # Check if the line has the correct format
        if len(parts) >= 9:
            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = parts[-2]
            # Update total file size
            total_file_size += file_size
            # Update status code counts
            if status_code.isdigit():
                status_code = int(status_code)
                if status_code in status_counts:
                    status_counts[status_code] += 1
            # Increment line count
            line_count += 1
        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code in sorted(status_counts.keys()):
                print(f"{code}: {status_counts[code]}")
            print()
except KeyboardInterrupt:
    # Handle keyboard interruption
    print("\nKeyboard interruption detected. Exiting...")
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

