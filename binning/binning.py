def cal_bin(x_1, x_min, num_bins, w):
    F_I = (x_1 - x_min)//w
    Fix_I = num_bins -1

    return min(F_I, Fix_I)
    
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    max_len = len(values)
    w = (values[max_len -1] - values[0])/num_bins
    bin_index = []
    min_value = values[0]
    max_value = values[max_len - 1]

    if max_value == min_value:
        return [0] * max_len

    for i in range(max_len):
        bin_index.append(cal_bin(values[i], min_value, num_bins, w))

    return bin_index
    
