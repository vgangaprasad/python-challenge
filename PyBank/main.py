# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    next(csvreader, None)
    
    noofmonths = 0
    totalamount = 0
    prevmonthamt = 0
    currmonthamt = 0
    
    totalchange = 0
    currentdiff = 0
    maxposdiff = 0
    maxnegdiff = 0


    # Read each row of data after the header
    for row in csvreader:
        noofmonths = noofmonths + 1
        totalamount = totalamount + int(row[1])
        currmonthamt = int(row[1])
        if noofmonths != 1:
            currentdiff = currmonthamt - prevmonthamt
            totalchange = totalchange + (currentdiff)
            if currentdiff > 0:
                if currentdiff > maxposdiff:
                    maxposdiff = currentdiff
                    maxposmonth = row[0]
            elif currentdiff < 0:
                if currentdiff < maxnegdiff:
                    maxnegdiff = currentdiff
                    maxnegmonth = row[0]
        prevmonthamt = currmonthamt

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total months : {noofmonths}")
    print(f"Total : {totalamount}")
    print(f"Average Change: {round(totalchange/(noofmonths-1),2)}")
    print(f"Greatest Increase in Profits: {maxposmonth} (${maxposdiff})")
    print(f"Greatest Decrease in Profits: {maxnegmonth} (${maxnegdiff})")