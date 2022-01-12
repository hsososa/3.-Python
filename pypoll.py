import os
import csv

election_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')

id = []
county = []
candidate = []
cand_list = []
cand_votes = []

with open(election_csv) as csvfile:

    print(f"Election Results")
    election_data = csv.reader(csvfile,delimiter=',')

    header = next(election_data)
    
    for row in election_data:
        id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    print('-------------------------')

    # Calculating the total number of votes cast
    total_votes = len(id)
    print(f"Total Votes: {total_votes}")

    # Compile a complete list of candidates who received votes
    cand_set = sorted(set(candidate))
        # alphabetized the set with "sorted" because without it, the candidates would be compiled in a random order
    cand_list = list(cand_set)
 #   print(cand_list)

    ## Determining the percentage of votes and total number of votes for each candidate
    # initialize vote counters
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    tooley_votes = 0

    # loop through candidate list to count votes for each candidate
    for i in range(0,len(candidate)):
        if candidate[i] == "Khan":
            khan_votes += 1
        if candidate[i] == "Correy":
            correy_votes += 1
        if candidate[i] == "Li":
            li_votes += 1
        if candidate[i] == "O'Tooley":
            tooley_votes += 1
 
    # calculate vote percentage using candidate and total vote counts
    khan_percent = (khan_votes/total_votes)*100
    correy_percent = (correy_votes/total_votes)*100
    li_percent = (li_votes/total_votes)*100
    tooley_percent = (tooley_votes/total_votes)*100
    
    print('-------------------------')
    print(f"{cand_list[0]}: {correy_percent: .3f}% ({correy_votes})")
    print(f"{cand_list[1]}: {khan_percent: .3f}% ({khan_votes})")
    print(f"{cand_list[2]}: {li_percent: .2f}% ({li_votes})")
    print(f"{cand_list[3]}: {tooley_percent: .2f}% ({tooley_votes})")
    print('-------------------------')

    # Determining the winner of the election based on popular vote
    winner = max(cand_set, key = candidate.count)
    print(f"Winner: {winner}")

    # Outpuuting a text file with results of analysis
    output_path = os.path.join("PyPoll", "Analysis", "vote_analysis.txt")

    with open(output_path, "w") as f:
        f.write(f"Election Results \n------------------------- \
            \nTotal Votes: {total_votes} \
            \n------------------------- \
            \n{cand_list[0]}: {correy_percent: .3f}% ({correy_votes}) \
            \n{cand_list[1]}: {khan_percent: .3f}% ({khan_votes}) \
            \n{cand_list[2]}: {li_percent: .2f}% ({li_votes}) \
            \n{cand_list[3]}: {tooley_percent: .2f}% ({tooley_votes}) \
            \n------------------------- \
            \nWinner: {winner}")