# Importing dependencies
import os
import csv

# Creating a variable that will hold the CSV path
csvpath = os.path.join('Resources','budget_data.csv')

# Creating variables to hold the month and profit values
months = 0
profit = 0
greatest_profit = 0
worst_loss = 0

# Opening and reading the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
 
 # Skipping header row   
    csvheader = next(csvreader)
    
 # Creating a text file for the results/output
    results_file = open('pybank_analysis.txt', 'w')
    
    print('Financial Analysis')
    print('----------------------')

# Iterating and calculating the results    
    for row in csvreader:
        months += 1
        if int(row[1]) != 0:
            profit += int(row[1])
        if int(row[1]) != 0:
            average_change = profit/months
        if int(row[1]) > greatest_profit:
            greatest_profit = int(row[1])
            greatest_month = row[0]
        if int(row[1]) < worst_loss:
            worst_loss = int(row[1])
            worst_month = row[0]
  
# Printing out all results          
    print(f'Total Months: {months}')
    print(f'Total: ${profit}')
    print(f'Average Change: ${round(average_change,2)}')
    print(f'Greatest Increase in Profits: {greatest_month} (${greatest_profit})')
    print(f'Greatest Decrease in Profits: {worst_month} (${worst_loss})')

# Writing out all results
    results_file.write(f'Total Months: {months} \n')
    results_file.write(f'Total: ${profit} \n')
    results_file.write(f'Average Change: ${round(average_change,2)} \n')
    results_file.write(f'Greatest Increase in Profits: {greatest_month} (${greatest_profit}) \n')
    results_file.write(f'Greatest Decrease in Profits: {worst_month} (${worst_loss}) \n')