
## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, Python script has been created for analyzing the financial records of your company. use the dataset  of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 

* Python script  analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* Analysis is reported as follows: 

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, script prints the analysis to the terminal and export a text file with the results.

## PyPoll

![Vote-Counting](Images/Vote_counting.png)

* This challenge is to help a small, rural town modernize its vote-counting process. 

* Poll data from [election_data.csv](PyPoll/Resources/election_data.csv) is used for this analysis. The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

* Python script analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* And reports the following in terminal as well as log.txt file. 

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```
