#I am aware of my assault on best practices. I am very sorry. I'd be happy to discuss or fix those points at a date other than tonight.
#I'm just too tired to refactor this right now. If I told you that my laptop died, then when that worked the internet immediately died, then I had to give a tour to foundation students; I'm not sure you'd believe me.
#Anyhow, to cut a long introduction short, this was written with the aid of no one, and using no Python concepts I didn't already know. I didn't cheat just because I'm handing it in by the end of the day. Promise.

status = 0
#Here's a key for the status values (checking for year beyond 2017):
# Status 0 is: Not assigned
# Status 1 is: Assigned
# Status 2 is: Reopened
# Status 3 is: Passed

current_highest_percent = -1.0
current_lowest_percent = 101.0
winner = None
loser = None
#Those four are used when comparing the percentages of on-time trips


def yearChecker(info_to_check):
    for entry in info_to_check:
        year = entry[0]
        if year > 2017:
            return False
    return True
#Checks if the list has a year beyond 2017


while status != 3:
    if status == 0:
        usr_input = usr_input = input("Enter trips info: ")
        info = eval(usr_input)
        status = 1

    if status == 2:
        usr_input = input("Error! Enter trips info: ")
        info = eval(usr_input)
        status = 1

    if status == 1:
        if yearChecker(info) is True:
            status = 3
        if yearChecker(info) is False:
            status = 2


            
#This is a mess of hard-coded ASCII, it's very ugly
print("")
print("|   Year   |   Trips   |   Delayed   |   %on-time   |")
for entry in info:
    percent = ((entry[1]-entry[2])/entry[1]) * 100
    percent_rounded = round(percent, 2)
    
    print("|   " + str(entry[0]) + (7-len(str(entry[0]))) * " " + "|    " + str(entry[1]) +  (7-len(str(entry[1]))) * " " + "|     " + str(entry[2]) + (8-len(str(entry[2]))) * " " + "|    " + str(percent_rounded) + "%" + (9-len(str(percent_rounded))) * " " + "|" )

    #since we're looping over them here, might as well do a comparison
    
    if percent > current_highest_percent:
        winner = entry[0]
        current_highest_percent = percent

    if percent < current_lowest_percent:
        loser = entry[0]
        current_lowest_percent = percent

print("")
    
if winner is None or loser is None:
    print("Something is wrong with the trip numbers")
else:
    print("Best on-time year is: " + str(winner))
    print("Worst on-time year is: " + str(loser))


print("")


query_year = input("Please enter a year: ")
for entry in info:
    year = entry[0]
    if year == int(query_year):
        print("Year " + query_year + ": " + "total trips = " + str(entry[1]) + ", on-time trips = " + str(entry[1]-entry[2])) 
