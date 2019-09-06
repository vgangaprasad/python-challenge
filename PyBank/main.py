# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    noofmonths = 0
    totalamount = 0
    prevmonthamt = 0
    currmonthamt = 0
    change = 0
    # Read each row of data after the header
    for row in csvreader:
        noofmonths = noofmonths + 1
        totalamount = totalamount + int(row[1])
        currmonthamt = int(row[1])
        if noofmonths != 1:
            change = change + (currmonthamt - prevmonthamt)
            print(change)
        prevmonthamt = currmonthamt

    print(f"No of months : {noofmonths}")
    print(f"Total Amount: {totalamount}")
    print(f"Average Change: {round(change/(noofmonths-1),2)}")



