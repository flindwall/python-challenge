import os
import csv

#Total Vote Counter
total_votes=0

#Candidate Options and Vote Counters
candidate_names = []
candidate_votes={}

#create path for csv file and slice the file so that the reader starts at first row
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, 'r') as csvfile:
    reader=list(csv.reader(csvfile, delimiter = ","))[1:]

    for row in reader:
        #print(". ", end="")
        #Add to total vote count
        total_votes+=1
        #find candidate name from each row in column 3
        candidate_name=row[2]
        #find new candidate names and add to the list
        if candidate_name not in candidate_names:
            #add to list of possible candidates in the race
            candidate_names.append(candidate_name)
            #track vote count
            candidate_votes[candidate_name]=0

        #add to vote count
        candidate_votes[candidate_name]=candidate_votes[candidate_name] + 1
    
    #access candidate votes dictionary to find the most number of votes to determine winner
    winner = max(candidate_votes, key= candidate_votes.get)
    #print(winner)

print("Election Results")
print("----------------")
print("Total Votes :"+ " " + str(total_votes))
print("----------------")

#retreive candidate and their corresponding vote count and percentage of votes
for candidate, votes in candidate_votes.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")

print("-----------------")
print("Winner :" + " " + str(winner))
print("-----------------")

#export as text file
with open('election_analysis.txt', 'w') as text:
    text.write("Election Results" + "\n")
    text.write("----------------" + "\n")
    text.write("Total Votes :"+ " " + str(total_votes)+ "\n")
    text.write("----------------" + "\n")
    text.write(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")" + "\n")
    text.write("----------------" + "\n")
    text.write("Winner :" + " " + str(winner) + "\n")
    text.write("----------------" + "\n")







