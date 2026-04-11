import math
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    return [math.log(1+v) for v in values]