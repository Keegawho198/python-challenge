import pandas as pd

import sys
import os

# Create the 'Analysis' folder if it doesn't exist
if not os.path.exists('Analysis'):
    os.makedirs('Analysis')

# Define the path to the output file
output_file = 'analysis/testText.txt'

# Redirect the standard output to the file, write into this text doc
sys.stdout = open(output_file, 'w')




# Load the dataset
data = pd.read_csv('Resources/budget_data.csv')

# Count the total number of months in the "Date" column
total_months = len(data['Date'])

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period and add it as a new column
#we create a new coloumn in dataset called profit/loss change where we store the value for diff.
#we have to store this value away as we will not be able to check it with other values to see differences each month.
data['Profit/Losses Change'] = data['Profit/Losses'].diff()

# Calculate the average of the changes in "Profit/Losses changes coloumn that we made"
average_change = data['Profit/Losses Change'].mean()

# Find the row with the biggest increase in profits
max_increase_row = data.loc[data['Profit/Losses Change'] == data['Profit/Losses Change'].max()]

# Extract the date and amount of the biggest increase in profits
#.values[0] returns the first value back from array
biggest_increase_date = max_increase_row['Date'].values[0]
biggest_increase_amount = max_increase_row['Profit/Losses Change'].values[0]

# Find the row with the lowest decrease in profits
min_decrease_row = data.loc[data['Profit/Losses Change'] == data['Profit/Losses Change'].min()]

# Extract the date and amount of the biggest increase in profits
#.values[0] returns the first value back from array
lowest_decrease_date = min_decrease_row['Date'].values[0]
lowest_decrease_amount = min_decrease_row['Profit/Losses Change'].values[0]


# Outputs
print("")
print("Financial Analysis")
print("")

print("-------------------------------")
print("")

print("Total months:", total_months)
print("")

print("Net Total: $", net_total)
print("")

print("Average Change: $", average_change)
print("")


#print("Greatest Increase in Profits")
#print("Date:", biggest_increase_date)
#print("Amount: $", biggest_increase_amount)
print(f"Greatest Increase in Profits: {biggest_increase_date} ${biggest_increase_amount:.2f}")
print("")



#print("Lowest Decrease in Profits")
#print("Date:", lowest_decrease_date)
#print("Amount: $", lowest_decrease_amount)
print(f"Greatest Decrease in Profits: {lowest_decrease_date} ${lowest_decrease_amount:.2f}")
print("")


#print(data['Profit/Losses Change'])


# Close the file after writing
sys.stdout.close()

# Reset the standard output to the console
sys.stdout = sys.__stdout__
