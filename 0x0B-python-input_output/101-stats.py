#!/usr/bin/python3
"""
Script reads stdin line by line and computes metrics

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
total file size and
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500

format: File size: <total size>
format: <status code (in ascending order)>: <number>
"""

import sys


def print_size_and_codes(size, stat_codes):
    """
    Print the total file size and status code statistics.

    Args:
        size (int): Total file size.
        stat_codes (dict): A dictionary containing status
        codes and their counts.

    Prints:
        - File size: <total size>
        - <status code (in ascending order)>: <number>
    """
    print(f"File size: {size}")
    for code, count in sorted(stat_codes.items()):
        if count:
            print(f"{code}: {count}")


def parse_line(line, size, stat_codes):
    """
    Parse a single line and update the size
    and status code statistics.

    Args:
        line (str): The input log line to parse.
        size (int): Current total file size.
        stat_codes (dict): A dictionary containing status codes
        and their counts.

    Returns:
        int: Updated total file size.
        dict: Updated status code statistics.
    """
    fields = line.strip().split()
    size += int(fields[-1])
    if fields[-2] in stat_codes:
        stat_codes[fields[-2]] += 1
    return size, stat_codes


def parse_stdin_and_compute():
    """
    Read lines from stdin, parse them, and compute statistics.

    This function reads lines from stdin, parses them
    using the `parse_line` function, and keeps track of total file size
    and status code statistics. It prints these statistics every
    10 lines and handles KeyboardInterrupt to provide results
    in case of an interruption.
    """
    size = 0
    stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                  "404": 0, "405": 0, "500": 0}
    lines = 0

    try:
        for line in sys.stdin:
            size, stat_codes = parse_line(line, size, stat_codes)
            lines += 1
            if lines % 10 == 0:
                print_size_and_codes(size, stat_codes)
    except KeyboardInterrupt:
        print_size_and_codes(size, stat_codes)
        raise


if __name__ == "__main__":
    parse_stdin_and_compute()
