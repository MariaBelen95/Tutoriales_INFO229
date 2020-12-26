def get_min(values):
    _min = values[0]
    for val in values:
        if val < _min:
            _min = val
    return _min
