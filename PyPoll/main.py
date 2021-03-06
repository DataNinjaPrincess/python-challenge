#Dependencies
import os
import csv  

# Specify the file to read
DataPath = os.path.join("Resources","election_data.csv")

# initialize variables
Khan = 0 #vote count for candidate Khan
Correy = 0 #vote count for candidate Correy
Li = 0 #vote count for candidate Li
OTooley = 0 #vote count for candidate O'Tooley
total = 0 #running total of votes cast

#Open the file using read mode
with open(DataPath, 'r') as DataFile:

#Set up the reader with delimiter
    VoteData = csv.reader(DataFile, delimiter=',')
    
#Read the header row and make it go to the first data row
    Header = next(VoteData)

#Doing the actual work
    for row in VoteData:
        #increment month counter
        total = total + 1

        #Tally the Votes
        if row[2] == "Khan":
            Khan = Khan + 1
        else:
            if row[2]== "Correy":
                Correy = Correy +1
            else:
                if row[2]=="Li":
                    Li = Li + 1
                else:
                    OTooley = OTooley + 1
    
#winner loop
if max(Khan, Correy, Li, OTooley) == Khan:
    Winner = "Khan"
else:
    if max(Khan, Correy, Li, OTooley) == Correy:
        Winner = "Correy"
    else:
        if max(Khan, Correy, Li, OTooley) == Li:
            Winner = "Li"
        else:   
            Winner = "OTooley"

            #print to terminal
print ("Election Results")
print ("-------------------------")
print ("Total Votes: " + str(total))
print ("-------------------------")
print("Khan: " + str(format(round((Khan/total)*100,3),'.3f'))+"% (" + str(Khan)+")")
print("Correy: " + str(format(round((Correy/total)*100,3),'.3f'))+"% (" + str(Correy)+")")
print("Li: " + str(format(round((Li/total)*100,3),'.3f'))+"% (" + str(Li)+")")
print("O'Tooley " + str(format(round((OTooley/total)*100,3),'.3f'))+"% (" + str(OTooley)+")")
print("-------------------------")
print("Winner: " + Winner)
print("-------------------------")

# Print to text file
# Create file path
Summary = os.path.join("Analysis", "ElectionResults.txt")

# Open the file using read mode
with open(Summary, 'w') as SummaryTable:

    #realize I probably should have written a function for the first print, copy/paste a lot
    SummaryTable.writelines ("Election Results")
    SummaryTable.write('\n')
    SummaryTable.writelines("-------------------------")
    SummaryTable.write('\n')
    SummaryTable.writelines("Total Votes: " + str(total))
    SummaryTable.write('\n') 
    SummaryTable.writelines("-------------------------")
    SummaryTable.write('\n') 
    SummaryTable.writelines("Khan: " + str(format(round((Khan/total)*100,3),'.3f'))+"% (" + str(Khan)+")")
    SummaryTable.write('\n')
    SummaryTable.writelines("Correy: " + str(format(round((Correy/total)*100,3),'.3f'))+"% (" + str(Correy)+")")
    SummaryTable.write('\n')
    SummaryTable.writelines("Li: " + str(format(round((Li/total)*100,3),'.3f'))+"% (" + str(Li)+")")
    SummaryTable.write('\n')
    SummaryTable.writelines("O'Tooley " + str(format(round((OTooley/total)*100,3),'.3f'))+"% (" + str(OTooley)+")")
    SummaryTable.write('\n')
    SummaryTable.writelines("-------------------------")
    SummaryTable.write('\n')
    SummaryTable.write("Winner: " + Winner)
    SummaryTable.write('\n')
    SummaryTable.writelines("-------------------------")
    SummaryTable.write('\n')
