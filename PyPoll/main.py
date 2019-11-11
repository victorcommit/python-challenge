#Import Dependencies
import os 
import csv

# Specify the file path
votefile = os.path.join("..", "PyPoll", "election_data.csv")

#Delcare Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#Open the file, Specify the variable to hold the contents
with open(votefile,newline="", encoding="utf-8") as votecounts:

    #Store csv content as a variable "csvreader"
    csvreader = csv.reader(votecounts,delimiter=",")

    #Skip the header
    header = next(csvreader)

    #Iterate through each row in the csv
    for row in csvreader:

        #Count the unique Voter IDs and store information as "total_votes"
        total_votes +=1

        #If candidates name is found, count the times appears and store to list 
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

#Create a dictionary of unique Voter IDs 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]  

#Combine list of candidates adn votes and return winner with the max
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#Print candidate results in percentage
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

#Print the summary of results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#Create outfile path
results = os.path.join("..", "PyPoll", "Election_Results.txt")

#Open the output file, in "write"
with open(results,"w") as file:

#Write the results to the new csv fil "Election Results"
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")
