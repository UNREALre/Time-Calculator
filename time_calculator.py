def add_time(start, duration, start_day=None):
    start_time, day_period = start.split()
    start_h, start_m = map(int, start_time.split(':'))  # converting using map
    duration_h, duration_m = [int(x) for x in duration.split(':')]  # converting using list comprehension

    # performing basic hours/minutes operations
    res_m = start_m + duration_m
    res_h = start_h + duration_h + (res_m // 60)
    res_m = res_m % 60 if res_m >= 60 else res_m

    # am/pm corrections
    day_half_num = res_h // 12
    days_passed_str, days_passed = calculate_passed_days(day_half_num, day_period)
    res_h = res_h % 12 if day_half_num else res_h
    if day_half_num % 2 != 0:
        day_period = 'AM' if day_period == 'PM' else 'PM'

    new_day = get_new_day(start_day, days_passed) if start_day else ''

    return '{}:{:02d} {}{}{}'.format(12 if not res_h else res_h, res_m, day_period, new_day, days_passed_str)


def calculate_passed_days(half_nums, starting_daytime):
    """Получает кол-во раз по 12ч прошедших с изначального времени и начальное время дня (am/pm)"""

    days_passed = half_nums // 2
    if (not days_passed and half_nums and starting_daytime == 'PM') or \
            (half_nums % 2 != 0 and starting_daytime == 'PM'):
        days_passed += 1

    if days_passed == 1:
        ret = ' (next day)'
    elif days_passed > 1:
        ret = ' ({} days later)'.format(days_passed)
    else:
        ret = ''

    return ret, days_passed


def get_new_day(start_day, days_passed):
    start_day = start_day.lower()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    days_passed += days.index(start_day)
    new_index = days_passed % 7 if days_passed >= 7 else days_passed

    return ', {}'.format(days[new_index].title())
