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


def print_metrics(total_size, status_codes):
    """
    Print the total file size and status code statistics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): A dictionary containing status codes
        and their counts.

    Prints:
        - File size: <total size>
        - <status code>: <number>
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        count = status_codes.get(code, 0)
        if count > 0:
            print(f"{code}: {count}")


def main():
    """
    Read lines from stdin, parse them, and compute statistics.

    This function reads lines from stdin, parses them, keeps track
    of total file size, and counts status code occurrences.
    It prints these statistics every 10 lines and handles KeyboardInterrupt
    to provide results in case of an interruption.
    """
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
                    "404": 0, "405": 0, "500": 0}
    lines = 0

    try:
        for line in sys.stdin:
            fields = line.strip().split()
            if len(fields) >= 9:
                status_code = fields[-2]
                size = int(fields[-1])
                total_size += size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                lines += 1

                if lines % 10 == 0:
                    print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)


if __name__ == "__main__":
    main()
