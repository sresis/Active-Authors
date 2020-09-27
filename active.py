"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""


def most_active(bio_data):
    """Find window of time when most authors were active."""
    # get every possible window of time
    #authors need to be active the entire time
    #use a dict to store who is in there?
    time_windows = []
    for item in bio_data:
        time_windows.append(item[1])
        time_windows.append(item[2])

    time_windows.sort()
    all_options = []
    i = 0
    while i < len(time_windows):
        j = 0
        while j < len(time_windows):
            if time_windows[i] <= time_windows[j] and time_windows[i] != time_windows[j]:
                add = [time_windows[i], time_windows[j]]
                add = tuple(add)
                all_options.append(add)
            j += 1
        i += 1
    author_dict = {}
    for item in all_options:
        author_dict[item] = []
        for author in bio_data:
            if author[1] <= item[0] and author[2] >= item[1]:
                author_dict[item].append(author[0])
    max_count = 0
    best_dates = ()
    for item in author_dict:
        if len(author_dict[item]) > max_count:
            max_count = len(author_dict[item])
            best_dates = item
    return best_dates
            
    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")