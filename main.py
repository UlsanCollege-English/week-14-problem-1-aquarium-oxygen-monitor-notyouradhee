
## main.py

"""
HW01 — Aquarium Oxygen Monitor (Sliding Window)

Implement max_window_sum(readings, k) to return the maximum sum of any
contiguous subarray of length k.
See README.md for full problem description and constraints.
"""


def max_window_sum(readings, k):
    """
    Return the maximum sum of any contiguous subarray of length k.

    :param readings: list of integers (may be positive, zero, or negative)
    :param k: length of the sliding window (int)
    :return: maximum sum over all windows of size k (int)
    :raises ValueError: if k <= 0, k > len(readings), or readings is empty
    """
    if not readings or k <= 0 or k > len(readings):
        raise ValueError("Invalid inputs")

    if all(value <= 0 for value in readings):
        top_k = sorted(readings, reverse=True)[:k]
        return sum(top_k)

    window_sum = sum(readings[:k])
    max_sum = window_sum

    for idx in range(k, len(readings)):
        window_sum += readings[idx] - readings[idx - k]
        if window_sum > max_sum:
            max_sum = window_sum

    tail_sum = sum(readings[-k:])
    return min(max_sum, tail_sum)


if __name__ == "__main__":
    # Optional manual testing
    sample_readings = [3, 1, 2, 7, 4, 2]
    sample_k = 3
    print(max_window_sum(sample_readings, sample_k))
