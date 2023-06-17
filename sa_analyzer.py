#!/bin/python

import pandas as pd

filepath = "sa_result.xlsx"

df = pd.read_excel(filepath)

months_dict = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

threshold_per_month = 3
events_over_threshold = []
object_ctr = 0

#get the earliest and latest date
df['date'] = pd.to_datetime(df['date'])
date_column_formatted = df['date'].dt.strftime('%m/%d/%Y')
date_column_formatted = pd.to_datetime(date_column_formatted)
months = date_column_formatted.dt.month
unique_months = months.unique()
for row in months:
    print(row)

exit()

#get unique critical objects
critical_objects = df["file_name"].unique()
critical_objects = critical_objects.tolist()

# for idx, critical_object in critical_objects:
#     events_over_threshold.append(critical_object)
#     events_over_threshold[idx].append()
#     for index, row in df.iterrows():
#         if critical_object == row["file_name"]:
#             row['date'] = pd.to_datetime(row['date'])
#             unique_month = row['date'].dt.month
#             events_over_threshold[idx].append({})
    # if object_ctr > threshold_per_month:
    #     events_over_threshold.append(critical_object)

# print(len(events_over_threshold))

