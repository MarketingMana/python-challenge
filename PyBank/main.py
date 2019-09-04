#The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date Tand amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import csv
budget_data_csv = "budget_data.csv"

with open(budget_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # skip header
    next(csv_reader)
    
    month_counter = 0
    total_change = 0
    previous_row_value = 0
    average_total = 0
    min_change = 0
    max_change = 0
   

    for row in csv_reader: 
        month_counter = month_counter + 1
        total_change = total_change + int(row[1])
        current_row_value = int(row[1])
        
        if previous_row_value == 0: 
            pass
        else: 
            difference_value = current_row_value - previous_row_value
    
            if (difference_value > max_change):
                max_change = difference_value
                max_month = row[0]
        
            if (difference_value < min_change):
                min_change = difference_value
                min_month = row[0]
        
            average_total += difference_value
            
        previous_row_value = int(row[1])

    
    average_change = round(average_total / (month_counter - 1), 2)


    print("Financial Analysis")
    print("----------------------------")

    text_string= (

    f"\n Total Months : {month_counter} \n"
    f" Total Change: ${total_change}\n"
    f" Average Change: ${average_change}\n"
    f" Max Change: ${max_change} on {max_month}\n"
    f" Min Change: ${min_change} on {min_month}\n "
 )
    print (text_string)