import string


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


def validate_date(date):
    if len(date) != 10:
        return False

    for i in (0, 1, 3, 4, 6, 7, 8, 9):
        if date[i] not in string.digits:
            return False

    for i in (2, 5):
        if date[i] != '.':
            return False

    year_int = int(date[6:])
    month_int = int(date[3:5])
    day_int = int(date[0:2])

    if month_int > 12:
        return False

    if month_int in (1, 3, 5, 7, 8, 10, 12) and day_int > 31:
        return False

    if month_int in (4, 6, 9, 11) and day_int > 30:
        return False

    if month_int == 2:
        if is_leap_year(year_int):
            if day_int < 30:
                return True
            else:
                return False
        else:
            if day_int < 29:
                return True
            else:
                return False

    return True


assert validate_date('11.02.2022') == True
assert validate_date('1111111111') == False
assert validate_date('1') == False
assert validate_date('.') == False
assert validate_date('aa.aa.ffff') == False

assert validate_date('01.13.2009') == False
assert validate_date('-1.02.2009') == False
assert validate_date('31.04.2009') == False
assert validate_date('29.02.2009') == False
assert validate_date('28.02.2009') == True
assert validate_date('28.02.2012') == True
assert validate_date('29.02.2012') == True


#######################################################

def validate_time(time):
    if len(time) != 5 or time[2] != ':':
        return False

    if time[0] not in ('0', '1', '2'):
        return False
    if (time[0] == '0' or time[0] == '1') and time[1] not in string.digits:
        return False
    if time[0] == '2' and time[1] not in ('0', '1', '2', '3'):
        return False

    if time[3] not in ('0', '1', '2', '3', '4', '5'):
        return False
    if time[3] in ('0', '1', '2', '3', '4', '5') and time[4] not in string.digits:
        return False

    return True


assert validate_time('02:02') == True
assert validate_time('11:34') == True
assert validate_time('23:49') == True
assert validate_time('22:3') == False
assert validate_time('aa:23') == False
assert validate_time('3:333') == False
assert validate_time('02:61') == False
assert validate_time('24:22') == False
assert validate_time('24:61') == False
assert validate_time('41:00') == False
assert validate_time('44:00') == False
assert validate_time('44:5a') == False
assert validate_time('44:61') == False
