import calendar as cal

print(cal.weekheader(3))
print(cal.monthcalendar(2023, 6))


def prev_month_days(year, month):
    if month == 1:
        prev_month = cal.monthcalendar(year-1, 12)
    else:
        prev_month = cal.monthcalendar(year, month-1)

    return [[day for day in prev_month[-1] if day !=0]]


def next_month_days(year, month):
    if month == 12:
        next_month = cal.monthcalendar(year+1, 1)
    else:
        next_month = cal.monthcalendar(year, month+1)

    return [[day for day in next_month[0]]]

