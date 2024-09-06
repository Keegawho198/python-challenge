#PyPoll

import pandas as pd
import sys
import os

# Create the 'Analysis' folder if it doesn't exist
if not os.path.exists('Analysis'):
    os.makedirs('Analysis')

# Define the path to the output file
output_file = 'Analysis/Results.txt'

# Open the file in write mode
file = open(output_file, 'w')

# Function!!! to print to both the console and the file
def print_both(message):
    print(message)  # Print to console
    file.write(message + '\n')  # Writes to file, \n makes sure each line is on a new line.



# Load the dataset
data = pd.read_csv('Resources/election_data.csv')


#The total number of votes cast
total_votes = len(data['Ballot ID'])


#put unique candidates here
#candidates = []
candidates = data['Candidate'].unique()

# Group the data by candidate and count the number of votes each candidate received
#.value_counts counts each unique value happens to be there, and getting candidate value from 
#data['Candidate'] from excel file.
candidate_votes = data['Candidate'].value_counts()


# Calculate the percentage of votes each candidate won
candidate_percentages = (candidate_votes / total_votes) * 100


# Find the candidate with the most votes
winner = candidate_votes.idxmax()  # Get the index (candidate name) String value, with the maximum value



#Outputs
print_both("Election Results")

print_both("")
print_both(f"Total Votes: {total_votes}")
print_both("")


# Display the total votes and percentage of votes each candidate won
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print_both(f"{candidate}: {percentage:.2f}% {votes} votes")
    print_both("")

print_both(f"Winner: {winner}")



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