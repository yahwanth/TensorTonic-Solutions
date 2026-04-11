def calculate_bin_index(value, min_value, num_bins, bin_width):
    """Calculate the bin index for a single value."""
    raw_index = int((value - min_value) // bin_width)
    max_index = num_bins - 1
    return min(raw_index, max_index)


def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.

    Args:
        values (list): Sorted list of numeric values.
        num_bins (int): Number of bins to divide the range into.

    Returns:
        list: A list of 0-indexed bin assignments.
    """
    # Edge case: all values identical
    if values[-1] == values[0]:
        return [0] * len(values)

    bin_width = (values[-1] - values[0]) / num_bins

    return [
        calculate_bin_index(v, values[0], num_bins, bin_width)
        for v in values
    ]
