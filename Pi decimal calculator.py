import math
def PI_Calculator(user_input):
    desired_answer=round(math.pi,user_input)
    calculation=0
    iterator=1
    while round(math.sqrt(calculation),user_input)!= round(math.pi,user_input):
        function=6/(iterator**2)
        calculation+=function
        iterator+=1
    Answer=round(math.sqrt(calculation),user_input)
    print(Answer)

import datetime
def day_calc():
    date_entry = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)

    day_number = (date1 - datetime.date(date1.year, 1, 1)).days + 1

    print("Day", day_number, "of the year")

day_calc()