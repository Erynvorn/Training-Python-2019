rom datetime import timedelta

def elapsed_seconds(start, end):
    return timedelta.total_seconds(end-start)


def elapsed_seconds(start, end):
    return (end - start).total_seconds()
