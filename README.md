# python-challenge

Keegan Nair


For printing output into a textfile and console, I used a function to print to both, Its called print_both.

So when we go to print output, instead of doing print("example text")

We do print_both("Example text")





Personal note for future use.

When using 

data['Profit/Losses Change'] = data['Profit/Losses'].diff()

To certain values and have them stored. We put them into a new coloumn, in this case it would be a new coloumn called profit/loss change. it will store our values there and we use these values to compare it with future values.



To find unique values in a coloum

We use 

candidates = data['Candidate'].unique()



To find out how much each unique value has we use

 candidate_votes = data['Candidate'].value_counts()


Find the candidate with the most votes
winner = candidate_votes.idxmax()  # Get the index (candidate name) String value, with the maximum value



Leaving those notes here, I believe they are the most important and I had difficulty having to find thises solutions. so putting it here in case I need a ref.
