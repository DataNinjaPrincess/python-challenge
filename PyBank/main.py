# Dependencies
import os
import csv

# Specify the file to read
DataPath = os.path.join("Resources","budget_data.csv")

# initialize variables
current = 0 #current month P&L
prior = 0 #prior month P&L
change = 0 #change between prior and current month P&L values
maxinc = 0 #varialbe to hold the maximum increase in P&L between months
maxdec = 0 #varlaine to hold the maximum decrease in P&L between months
months = 0 #counter for total number of months
total = 0 #running total of P&L changes
changesum = 0 #sum of change values, to determine average change
maxmo = 0 #time period value of the month with the maximum increase
minmo = 0 #time period value of the month with the maximum decrease

#Open the file using read mode
with open(DataPath, 'r') as DataFile:

#Set up the reader with delimiter
    BudgetData = csv.reader(DataFile, delimiter=',')
    
#Read the header row and make it go to the first data row
    Header = next(BudgetData)

    
#Doing the actual work
    for row in BudgetData:
        #increment month counter
        months = months + 1
        
        #set current month
        current = row[1]
        
        #if statement to exclude first month
        if prior == 0:
            change = 0
        else:
            #calculate the change
            change = int(current) - int(prior)
        
        #increment running total
        total = int(total) + int(current)
        
        #increment change total
        changesum = int(changesum) + int(change)
        
        #another if to account for that first month
        if prior == 0:
            avechg = 0    
        else:
            #make the average
            avechg = int(changesum)/(int(months)-1)
        
        #direct increase/decreases appropriately
        if change > 0 :
            if change>maxinc:
                maxinc = change
                maxmo = row[0]
        else:
            if change<maxdec:
                maxdec = change
                minmo = row[0]
        
        #when it's all done make the current prior and go around again
        prior = current
        
#print to terminal

print("Financial Analysis")
print ("-----------------------------")
print ("Total Months: " + str(months))  
print ("Total Profit: $" + str(total))
print ("Average Change: $" + str(round(avechg,2)))
print ("Greatest Increase in Profits: " + str(maxmo) +", $"+ str(maxinc) )
print ("Greatest Decrease in Profits: " + str(minmo) +", $"+ str(maxdec) )          


# Print to text file
# Create file path
Summary = os.path.join("Analysis", "FinancialSummary.txt")

# Open the file using read mode
with open(Summary, 'w') as SummaryTable:

    #realize I probably should have written a function for the first print, copy/paste a lot
    SummaryTable.writelines ("Financial Analysis")
    SummaryTable.write('\n')
    SummaryTable.writelines("-----------------------------")
    SummaryTable.write('\n')
    SummaryTable.writelines("Total Months: " + str(months))
    SummaryTable.write('\n') 
    SummaryTable.writelines("Total Profit: $" + str(total))
    SummaryTable.write('\n')
    SummaryTable.writelines("Average Change: $" + str(round(avechg,2)))
    SummaryTable.write('\n')
    SummaryTable.writelines("Greatest Increase in Profits: " + str(maxmo) +", $"+ str(maxinc) )
    SummaryTable.write('\n')
    SummaryTable.writelines("Greatest Decrease in Profits: " + str(minmo) +", $"+ str(maxdec) )  