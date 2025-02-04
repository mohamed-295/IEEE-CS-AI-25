#Problem 2
Day=int(input("Enter the day: "))
Month=int(input("Enter the month: "))
Year=int(input("Enter the year: "))

months ={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

if int(Year)%4==0:
    months[2]=29

Nday = Day+7
Nmonth = Month
Nyear = Year
if Nday>months[Month]:
    Nday = Nday-months[Month]
    Nmonth+=1
    if Nmonth>12:
        Nmonth = 1
        Nyear+=1

print(f'Day: {Nday} Month: {Nmonth} Year: {Nyear}')