# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import sys
# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')


# This function is used for calculating the percentage of votes
def calculate_percent(count = 0, totalcount = 0):
    return round((count/totalcount) * 100,3)

#CSV File will be opened and processed here
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
        #increment the totalvotes variable for each row read
        totalvotes = totalvotes + 1
        # Checking if Candidate is already added to the dictionary.
        # if not added, candidate name is added and set key (vote count) value to 1 
        # If candidate already present, then increment the key value (vote count) by 1
        if row[2] in candidate_dict.keys():
            candidate_dict[f'{row[2]}'] += 1 
        else:
            candidate_dict.update({f'{row[2]}' : 1})


# This function is used to print the winner
def printoutput():
    winner = ""
    winnercount = 0
    print("Election Results")
    print("----------------------------")
    print(f"Total votes: {totalvotes}")
    print("----------------------------")

#This for loop will print each candidate in the dictionary with the following information
# Name
# Vote Percentage
# number of votes
# and finally the winner
    for candidate in candidate_dict:
        print(f"{candidate} : \
{calculate_percent(candidate_dict[candidate],totalvotes)}00% \
({candidate_dict[candidate]})") 
        # winner is identified in this logic, for every value in dictionary, it is compared with the 
        # previous dictionary value and winner is decided based on whichever key has the most number 
        # of votes
        if winnercount < candidate_dict[candidate]:
            winnercount = candidate_dict[candidate]
            winner = candidate
    
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

# printoutput function is called here to print the winner in the expected format
printoutput()
# printoutput function is called here again to print the winner in the expected format in an
# output file
sys.stdout = open('log.txt', 'w')
printoutput()
