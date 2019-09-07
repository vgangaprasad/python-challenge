# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import sys
# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    next(csvreader, None)
    candidates = []
    candidate_dict = {}
    #long totalvotes
    totalvotes = 0
    # Read each row of data after the header
    for row in csvreader:
        totalvotes = totalvotes + 1
        if row[2] in candidate_dict.keys():
            candidate_dict[f'{row[2]}'] += 1 
        else:
            candidate_dict.update({f'{row[2]}' : 1})

def calculate_percent(count = 0, totalcount = 0):
    return round((count/totalcount) * 100,3)

def printoutput():
    winner = ""
    winnercount = 0
    print("Election Results")
    print("----------------------------")
    print(f"Total votes: {totalvotes}")
    print("----------------------------")
    #print(candidate_dict)
    for candidate in candidate_dict:
        print(f"{candidate} : \
{calculate_percent(candidate_dict[candidate],totalvotes)}00% \
({candidate_dict[candidate]})") 
        if winnercount < candidate_dict[candidate]:
            winnercount = candidate_dict[candidate]
            winner = candidate
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")


        #print(candidate)


printoutput()
sys.stdout = open('log.txt', 'w')
printoutput()
