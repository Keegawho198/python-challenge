#PyBank
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
    file.write(message + '\n')  # Writes to file


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
#.values[0] returns the first value back from arraybiggest_increase_date = max_increase_row['Date'].values[0]
biggest_increase_date = max_increase_row['Date'].values[0]
biggest_increase_amount = max_increase_row['Profit/Losses Change'].values[0]

# Find the row with the lowest decrease in profits
min_decrease_row = data.loc[data['Profit/Losses Change'] == data['Profit/Losses Change'].min()]

# Extract the date and amount of the lowest decrease in profits
#.values[0] returns the first value back from array
lowest_decrease_date = min_decrease_row['Date'].values[0]
lowest_decrease_amount = min_decrease_row['Profit/Losses Change'].values[0]

# Outputs
#calling function to print both to console and text file
print_both("")
print_both("Financial Analysis")
print_both("")

print_both("-------------------------------")
print_both("")

print_both(f"Total months: {total_months}")
print_both("")

print_both(f"Net Total: ${net_total}")
print_both("")

print_both(f"Average Change: ${average_change:.2f}")
print_both("")

print_both(f"Greatest Increase in Profits: {biggest_increase_date} ${biggest_increase_amount:.2f}")
print_both("")

print_both(f"Greatest Decrease in Profits: {lowest_decrease_date} ${lowest_decrease_amount:.2f}")
print_both("")


# Close the file after writing
file.close()
