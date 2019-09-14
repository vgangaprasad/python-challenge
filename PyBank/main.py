# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import sys
# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

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
        # number of months is calculated based on the number of rows
        noofmonths = noofmonths + 1
        # total amount variable is used to track the total amount from all the rows.
        totalamount = totalamount + int(row[1])
        #currmonthamt variable is used to save the amount from the current row.
        currmonthamt = int(row[1])
        # Following logic is used to find out the Greatest increase/decrease in profits
        if noofmonths != 1:
            # currentdiff variable is used to find out the amount difference between the
            # current month and previous month
            currentdiff = currmonthamt - prevmonthamt
            #totalchange variable is used to find out the average difference in change
            totalchange = totalchange + (currentdiff)
            # Everytime there is a positive/negative difference, it is compared against the previous
            # positive/negative difference and if new one is more then the new one is set as the 
            # greatest increase/negative amount
            if currentdiff > 0:
                if currentdiff > maxposdiff:
                    maxposdiff = currentdiff
                    maxposmonth = row[0]
            elif currentdiff < 0:
                if currentdiff < maxnegdiff:
                    maxnegdiff = currentdiff
                    maxnegmonth = row[0]
        prevmonthamt = currmonthamt

def printoutput():
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total months: {noofmonths}")
    print(f"Total: {totalamount}")
    print(f"Average Change: {round(totalchange/(noofmonths-1),2)}")
    print(f"Greatest Increase in Profits: {maxposmonth} (${maxposdiff})")
    print(f"Greatest Decrease in Profits: {maxnegmonth} (${maxnegdiff})")


printoutput()
sys.stdout = open('log.txt', 'w')
printoutput()