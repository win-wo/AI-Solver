""""Use to clean and format data"""


def split_cases(data):
    """split data per entry"""
    return [s.strip() for s in data.splitlines()]
