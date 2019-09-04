# Your task is to create a Python script that analyzes the votes and calculates each of the following:
#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

import csv
csvpath = 'election_data.csv'

import sys
sys.stdout = open('poll_results.txt', 'w')

#writing csv file with delimiter
with open('election_data.csv', newline="") as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=",")

    # Starting votes = 0
    votes_cast = 0
 
    #Skip past header
    csvreader = csv.reader(csvfile)
    next(csvreader)

    #dictionary
    candidates = {}

    for row in csvreader:
        # Increment for each vote cast
        votes_cast += 1

        #if candidate name appears +1 if not, move on
        if row[2] in candidates:
                candidates[row[2]] += 1
        else:
                candidates.update({row[2]: 1})

# Winner has the most votes
winner = max(candidates, key=candidates.get)

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes_cast}")
print("-------------------------")

# Iterate through dictionary to print out all results
for candidate in candidates:
    print(f"{candidate}: {round((candidates[candidate] * 100)/votes_cast, 3)}% ({candidates[candidate]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")