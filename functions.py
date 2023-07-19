import calendar as cal



def prev_month_days(year, month):
    if month == 1:
        prev_month = cal.monthcalendar(year-1, 12)
    else:
        prev_month = cal.monthcalendar(year, month-1)

    return [[day for day in prev_month[-1] if day != 0]]


def next_month_days(year, month):
    if month == 12:
        next_month = cal.monthcalendar(year+1, 1)
    else:
        next_month = cal.monthcalendar(year, month+1)

    return [[day for day in next_month[0]]]



#############################
# import calendar as cal
# import tkinter as tk
# from tkinter import ttk
# from functions import *
#
# week_labels = ["Mon", "Tue", "Wen", "Thr", "Fri", "Sat", "Sun"]
#
#
# def show_calendar():
#     # Retrieve the year and month from the input fields
#     year = int(year_entry.get())
#     month = int(month_entry.get())
#
#     # Generate the calendar for the specified year and month
#     current_month = cal.monthcalendar(year, month)
#     prev_month = prev_month_days(year, month)
#     next_month = next_month_days(year, month)
#
#     # Display the calendar
#     for index, day in enumerate(week_labels):
#         label = ttk.Label(master=week_days_frame, text=day)
#         label.grid(row=0, column=index, padx=5, pady=3)
#
#
#     for day in month_frame.winfo_children():
#         day.destroy()
#
#
#
#     if current_month[0][0] == 0:
#         show_month_days(prev_month, 1)
#     show_month_days(current_month, 1, 4)
#     if len(current_month) == 6:
#         show_month_days(next_month, 6)
#     elif current_month[-1][-1] == 0:
#         show_month_days(next_month, 5)
#
#
# def show_month_days(month, starting_row, border=1):
#     row_number = starting_row
#     for week in month:
#         for index, day in enumerate(week):
#             if day != 0:
#                 button = tk.Button(master=month_frame, width=3, text=day, borderwidth=border)
#                 button.grid(row=row_number, column=index)
#         row_number += 1
#
#
# def increase(entry_field):
#     value = int(entry_field.get())
#     entry_field.delete(0, 'end')
#     entry_field.insert(0, str(value+1))
#
# def decrease(entry_field):
#     value = int(entry_field.get())
#     entry_field.delete(0, 'end')
#     entry_field.insert(0, str(value-1))
#
#
#
#

# # Create the main window
# window = tk.Tk()
# window.title("Choose a day")
#
# # Create a frame to hold the input fields
# input_frame = ttk.Frame(window)
# input_frame.pack()
#
# # Create the year label, buttons and entry field
# year_label = ttk.Label(input_frame, text="Year:")
# year_label.grid(row=0, column=1, padx=5)
#
# year_entry = ttk.Entry(input_frame, width=10)
# year_entry.grid(row=1, column=1, padx=5)
#
# year_decrease_btn = ttk.Button(input_frame, width=2, text="<", command=lambda: decrease(year_entry))
# year_decrease_btn.grid(row=1, column=0, padx=5)
#
# year_increase_btn = ttk.Button(input_frame, width=2, text=">", command=lambda: increase(year_entry))
# year_increase_btn.grid(row=1, column=2, padx=5)
#
#
#
# # Create the month label,buttons and entry field
# month_label = ttk.Label(input_frame, text="Month:")
# month_label.grid(row=0, column=4, padx=5)
#
# month_entry = ttk.Entry(input_frame, width=10)
# month_entry.grid(row=1, column=4, padx=5)
#
# month_decrease_btn = ttk.Button(input_frame, width=2, text="<", command=lambda: decrease(month_entry))
# month_decrease_btn.grid(row=1, column=3, padx=5)
#
# month_increase_btn = ttk.Button(input_frame, width=2, text=">", command=lambda: increase(month_entry))
# month_increase_btn.grid(row=1, column=5, padx=5)
#
#
# # Create the "Show Calendar" button
# show_button = ttk.Button(window, text="Show Calendar", command=show_calendar)
# show_button.pack(pady=10)
#
# # Create frames to hold weekday names and month view
# week_days_frame = ttk.Frame(window)
# week_days_frame.pack(pady=5)
#
# month_frame = ttk.Frame(window)
# month_frame.pack(pady=3)
#
#
#
# # Start the GUI event loop
# #window.mainloop()