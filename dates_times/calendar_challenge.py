import calendar

def countWeekDays(theyear, themonth, theday):
    print(theyear, themonth, theday)
    daycount = 0
    weeklist = calendar.monthcalendar(theyear, themonth)
    print(weeklist)
    for week in weeklist:
        if week[theday] != 0:
            daycount += 1
    return daycount

run = True
while(run):
    print("Which day of the week do you want to count?")
    print("0:Monday")
    print("1:Tuesday")
    print("2:Wednesday")
    print("3:Thursday")
    print("4:Friday")
    print("5:Saturday")
    print("6:Sunday")
    print("Or 'exit' to quit")

    theday = input("? ")
    if theday == "exit":
        run = False
        break
    day = int(theday)

    yearstr = input("Enter year: ")
    year = int(yearstr)

    monthstr = input("Enter month: ")
    month = int(monthstr)

    result = countWeekDays(year, month, day)
    print("There are " + str(result) + " of those days")
