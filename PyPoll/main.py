# Importing dependencies
import os
import csv

# Creating a variable that will hold the CSV path
csvpath = os.path.join('Resources','election_data.csv')

# Printing out the candidates
candidates = ['Khan', 'Correy', 'Li', "O'Tooley"]
print(f'Candidates: {candidates}')

# Establishing a variable that will count the votes for each candidate
khan = 0
correy = 0
li = 0
otooley = 0

# Opening and reading the CSV file
with open(csvpath, newline = '') as election_data_file:
    csvreader = csv.reader(election_data_file, delimiter = ',')

# Skipping header row
    csvheader = next(csvreader)
       
# Creating a text file for the results/output
    results_file = open('pypoll_analysis.txt', 'w')

# Iterating and calculating the results
    for row in csvreader:
        if str(row[2]) == str('Khan'):
            khan += 1
        if str(row[2]) == str('Correy'):
            correy += 1
        if str(row[2]) == str('Li'):
            li += 1
        if str(row[2]) == str("O'Tooley"):
            otooley += 1
            
    total_votes = khan + correy + li + otooley
    
# Print out all results
    print('Election Results')
    print('----------------------')
    print(f'Total Votes: {total_votes}')
    print(f'Khan: {"{:.2f}%".format(khan/total_votes * 100)} ({khan})')
    print(f'Correy: {"{:.2f}%".format(correy/total_votes * 100)} ({correy})')
    print(f'Li: {"{:.2f}%".format(li/total_votes * 100)} ({li})')
    print(f"O'Tooley: {'{:.2f}%'.format(otooley/total_votes * 100)} ({otooley})")
    print('----------------------')
    print(f'Winner: Khan')
    print('----------------------')
    
# Writing out all results in the text file
    results_file.write('Election Results \n')
    results_file.write('---------------------- \n')
    results_file.write(f'Total Votes: {total_votes} \n')
    results_file.write(f'Khan: {"{:.2f}%".format(khan/total_votes * 100)} ({khan}) \n')
    results_file.write(f'Correy: {"{:.2f}%".format(correy/total_votes * 100)} ({correy}) \n')
    results_file.write(f'Li: {"{:.2f}%".format(li/total_votes * 100)} ({li}) \n')
    results_file.write(f"O'Tooley: {'{:.2f}%'.format(otooley/total_votes * 100)} ({otooley}) \n")
    results_file.write('---------------------- \n')
    results_file.write(f'Winner: Khan \n')
    results_file.write('---------------------- \n')