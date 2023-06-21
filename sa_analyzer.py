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
objects_over_threshold = {}


df['date'] = pd.to_datetime(df['date'])
date_column_formatted = pd.to_datetime(df['date'])
months = date_column_formatted.dt.month
unique_months = months.unique()
unique_months = unique_months.tolist()

def init_months():
    gathered_months_dict = {}
    for month in unique_months:
        gathered_months_dict[months_dict[month]] = 0
    return gathered_months_dict

def loop_thru_sa(critical_object):
    iterated_months = init_months()
    for index, row in df.iterrows():
        #if crit object is the same as file name, then iterate the month
        
        if critical_object == row["file_name"]:
            #get the month of that critical object
            month = row["date"].month
            iterated_months[months_dict[month]] +=1
    return iterated_months


#get unique critical objects
critical_objects = df["file_name"].unique()
critical_objects = critical_objects.tolist()
# critical_objects = ["AugueAliquamErat.mov", "IdTurpisInteger.pdf"]



#loop thru critical object and match it with file name in excel if it matches, then iterate the number of the specified month
for idx, critical_object in enumerate(critical_objects):
    objects_over_threshold[critical_object] = loop_thru_sa(critical_object)

#created new copied variable of objects since we are going to remove objects that has less logs
copied_objects_over_threshold = objects_over_threshold.copy()
   
for object, months in copied_objects_over_threshold.items():
    #if there is a month that has less than 3 logs for an object, then remove it
    for key1, month in months.items():
        if month < threshold_per_month:
            del objects_over_threshold[object]
            break
    

            
for key, value in objects_over_threshold.items():
    print(f"critical_object: {key}, \nLogs_per_month: {value}\n\n")
            
    
print(f"Kindly review this {len(objects_over_threshold)} critical_objects if they are really critical")


