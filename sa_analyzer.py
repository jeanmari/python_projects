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
gathered_months_dict = {}
threshold_per_month = 3
events_over_threshold = {}


df['date'] = pd.to_datetime(df['date'])
date_column_formatted = pd.to_datetime(df['date'])
months = date_column_formatted.dt.month
unique_months = months.unique()
unique_months = unique_months.tolist()

def init_months():
    for month in unique_months:
        gathered_months_dict[months_dict[month]] = 0
    return gathered_months_dict


#get unique critical objects
critical_objects = df["file_name"].unique()
critical_objects = critical_objects.tolist()
critical_objects = ["AugueAliquamErat.mov", "IdTurpisInteger.pdf"]


#loop thru critical object and match it with file name in excel if it matches, then iterate the number of the specified month
for idx, critical_object in enumerate(critical_objects):
    events_over_threshold[critical_object] = init_months()
    for index, row in df.iterrows():
        #if crit object is the same as file name, then iterate the month
        
        if critical_object == row["file_name"]:
            #get the month of that critical object
            month = row["date"].month
            #iterate the month in the dictionary
            events_over_threshold[critical_object][months_dict[month]] += 1
            
    # if idx == len(critical_objects):
    #     # print(critical_object) 
    #     break
    

# print(events_over_threshold["AugueAliquamErat.mov"])    
# for key, value in events_over_threshold.items():
#     print(f"critical_objects: {key}, \nValue: {value}\n\n")
events_over_threshold["IdTurpisInteger.pdf"] = {"January": 34, "February": 55, "March": 87}
print(events_over_threshold)

# print(len(events_over_threshold))

