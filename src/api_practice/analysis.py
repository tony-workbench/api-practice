"""Exercises on lists of HTTP status codes. Nothing here makes a network request.

Inputs are assumed to be well formed: records are (endpoint, int status) pairs
and statuses are ints. Invalid input is not checked.
"""


def count_failures(records):
    """Return {endpoint: number of records with status 400 or higher}."""
    counts = {}

    for endpoint, status in records:
        if status >= 400:
            counts[endpoint] = counts.get(endpoint, 0) + 1

    return counts


def api_error_summary(records):
    """Return (endpoint, failure count) pairs, most failures first, ties by name."""
    counts = count_failures(records)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))


def recovery_index(statuses, needed):
    """Return the index where the first run of `needed` 2xx statuses ends, or -1."""
    current_run = 0
    needed_run = needed
    for index, status in enumerate(statuses):
        if 200 <= status < 300:
            current_run += 1
            needed_run -= 1
            if needed_run == 0:
                break
        else:
            current_run = 0
            needed_run = needed
    if needed_run == 0:
        return index
    else:
        return -1
