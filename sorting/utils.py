def swap(arr, idx_1, idx_2):
    """
    Auxiliary function that swaps two values in an array.
    """

    # Temporary variable to store thw first value.
    temp = arr[idx_1]
    
    # Swapping values
    arr[idx_1] = arr[idx_2]
    arr[idx_2] = temp