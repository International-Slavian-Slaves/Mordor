from datetime import datetime, timedelta


def create_stack(query_array):
    """
    func creating stack for counting month hours
    """
    datetime_stack = []
    for tuple in query_array:
        pass_datetime = datetime.strptime(tuple[2], "%Y-%m-%d %H:%M:%S")
        pass_dir = tuple[3]
        datetime_tuple = pass_datetime, pass_dir
        if datetime_stack or pass_dir != 'out':  # de morgan rule was applied
            datetime_stack.append(datetime_tuple)
    return datetime_stack


def count_month_time(datetime_stack):
    """
    func counting month hours with the help of the stack
    """
    sum = 0
    current = None
    while datetime_stack:
        pass_datetime, pass_dir = datetime_stack.pop()
        if pass_dir == "in":
            if not current:
                current = pass_datetime
            delta = current - pass_datetime
            sum += delta.total_seconds()
        elif pass_dir == "out":
            current = pass_datetime
    return timedelta(seconds=sum).__str__()
