#note to graders- I've been having issues with the relative path of the budget data in the resources folder.
#If I open up the resources folder manually in VS Code next to the python file, then the code runs.

import os
import csv

#create pathway for csv file
#csvpath= /Users/franklindwall/Desktop/PythonStuff/Project2/Resources/budget_data.csv
csvpath= os.path.join("Resources", "budget_data.csv")

#access csvpath and slice file to start at the first row of data
with open(csvpath) as csv_file:
    reader= list(csv.reader(csv_file))[1:]
   
#create list of months column
# create list for amount column
# print statements are to ensure that lists are created and calculations are correct 
# I will comment out print statements throughout the code
months=[row[0]for row in reader]
amount = [int(row[1]) for row in reader]

total_months = len(months)

total=sum(amount)

#create loop to display consecutive profit/loss between columns and calculate the difference
#for i in range(len(amount)-1):
    #print(i, amount[i], i + 1, amount[i +1], amount[i+1]-amount[i])

differences=[amount[i+1]-amount[i]for i in range(len(amount)-1)]

#calculate average difference of profit and loss for 85 profit/losses changes
average_diff=sum(differences)/85
#print(average_diff)

#use min and max function to find the greatest increase and greatest decrease
greatest_increase=max(differences)
#print(greatest_increase)

greatest_decrease=min(differences)
#print(greatest_decrease)

greatest_month_increase_index= differences.index(greatest_increase)
greatest_increase_month= months[greatest_month_increase_index]
#print(greatest_increase_month)

#index the month of greatest increase and greatest decrease
greatest_month_decrease_index= differences.index(greatest_decrease)
greatest_decrease_month= months[greatest_month_decrease_index]
#print(greatest_decrease_month)

#print results to match the format of the homework rubric
print("Financial Analysis")
print("------------------")
print("Total Months:" + " " + str(total_months))
print("Total:" + " " + "$" + str(total))
print("Average Change:" + " " + "$" + str(average_diff))
print("Greatest Increase in Profits:" + " " + str(greatest_increase_month)+ " " + "($" + (str(greatest_increase)) + ")")
print("Greatest Decrease in Profits:" + " " + str(greatest_decrease_month)+ " " + "($" + (str(greatest_decrease)) + ")") 

#export results as text file 
with open('financial_analysis.txt', 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------\n")
    text.write("Total Months:" + str(total_months) + "\n")
    text.write("Total Profits:" + "$" + str(total) + "\n")
    text.write("Average Change:" + "$" + str(int(average_diff)) + "\n")
    text.write("Greatest Increase in Profits:"+ str(greatest_increase_month)+ "($" + str(greatest_increase)+")\n")
    text.write("Greatest Decrease in Profits:"+ str(greatest_decrease_month)+ "($" + str(greatest_decrease)+")\n")