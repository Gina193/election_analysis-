#The data we need to retrieve.
#1. The total number of votes cast 
#2. A complete list of candidates who recived votes
#3. The percentage of votes each candidate won 
#4. The total number of votes each candidte won 
#5. The winner of the election based on popular vote.
import csv
import os

# Assign Variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# openthe election results and read the file.
with open(file_to_load) as election_data:

    # to do: perform analysis.
    print(election_data)

    # Close the file.
election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()
 
  # Write three counties to the file.
     txt_file.write("Arapahoe, ")
     txt_file.write("Denver, ")
     txt_file.write("Jefferson")
        # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")
     import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)