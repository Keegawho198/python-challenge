#PyPoll

import pandas as pd
import sys
import os



# Load the dataset
data = pd.read_csv('Resources/election_data.csv')


#The total number of votes cast
total_votes = len(data['Ballot ID'])


#put unique candidates here
#candidates = []
candidates = data['Candidate'].unique()

# Group the data by candidate and count the number of votes each candidate received
#.value_counts counts each unique value happens to be there
candidate_votes = data['Candidate'].value_counts()


# Calculate the percentage of votes each candidate won
candidate_percentages = (candidate_votes / total_votes) * 100


# Find the candidate with the most votes
winner = candidate_votes.idxmax()  # Get the index (candidate name) with the maximum value



#Outputs
print("")
print(f"Total Votes: {total_votes}")
print("")


# Display the total votes and percentage of votes each candidate won
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print(f"{candidate}: {percentage:.2f}% {votes} votes")
    print("")

print(f"{winner}")

print(f"The winner is: {winner} with {candidate_votes[winner]} votes")


#Spare testing

# Print the list of candidates using loop to only use one of each candidate
#using loop because candidates are in a array because of unique()
#print("List of candidates who received votes:")
#for candidate in candidates:
    #print("")
    # print(candidate)
    
    #print(candidates)

#print(candidate_votes)
#print(candidate_percentages)

# Display the percentage of votes each candidate won
#for candidate, percentage in candidate_percentages.items():
 #   print(f"{candidate}: {percentage:.3f}%")