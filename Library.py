def print_change(initial, changed, prefix=""): 
    """  """
    difference = value_2 - value_1
    percent = - (1 - value_2 / value_1) * 100
    percent = "{:.2f}".format(percent)
    print(f'{prefix} {percent}%  \u25BC {difference} ({value_1} -> {value_2})')
    return value_2
