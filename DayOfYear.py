# File: DayOfYear.py
# Student: Malik Knight     
# UT EID: MJK3327
# Course Name: CS303E
# 
# Date: 02/12/2024
# Description of Program: The program will recieve an input for valid inputs of day month and year and return the exact day of the year. if an invalid input is entered the program will return invalid date.

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def computeOrdinalDate(year, month, day):
    JAN_DAYS = 31
    FEB_DAYS = 29 if isLeapYear(year) else 28
    MAR_DAYS = 31
    APR_DAYS = 30
    MAY_DAYS = 31
    JUN_DAYS = 30
    JUL_DAYS = 31
    AUG_DAYS = 31
    SEP_DAYS = 30
    OCT_DAYS = 31
    NOV_DAYS = 30
    DEC_DAYS = 31
    
    if month < 1 or month > 12:
        print("Illegal date entered!")
        return
    
   
    if (month == 1 and (day < 1 or day > JAN_DAYS) or
        month == 2 and (day < 1 or day > FEB_DAYS) or
        month == 3 and (day < 1 or day > MAR_DAYS) or
        month == 4 and (day < 1 or day > APR_DAYS) or
        month == 5 and (day < 1 or day > MAY_DAYS) or
        month == 6 and (day < 1 or day > JUN_DAYS) or
        month == 7 and (day < 1 or day > JUL_DAYS) or
        month == 8 and (day < 1 or day > AUG_DAYS) or
        month == 9 and (day < 1 or day > SEP_DAYS) or
        month == 10 and (day < 1 or day > OCT_DAYS) or
        month == 11 and (day < 1 or day > NOV_DAYS) or
        month == 12 and (day < 1 or day > DEC_DAYS)):
        print("Illegal date entered!")
        return
    
    ordinal_date = day
    if month >= 2: ordinal_date += JAN_DAYS
    if month >= 3: ordinal_date += FEB_DAYS
    if month >= 4: ordinal_date += MAR_DAYS
    if month >= 5: ordinal_date += APR_DAYS
    if month >= 6: ordinal_date += MAY_DAYS
    if month >= 7: ordinal_date += JUN_DAYS
    if month >= 8: ordinal_date += JUL_DAYS
    if month >= 9: ordinal_date += AUG_DAYS
    if month >= 10: ordinal_date += SEP_DAYS
    if month >= 11: ordinal_date += OCT_DAYS
    if month >= 12: ordinal_date += NOV_DAYS
    
    print(f"{month}/{day}/{year} is day {ordinal_date} of the year.")

def main():
    year = int(input("Specify a year: "))
    month = int(input("Specify a month (1-12): "))
    day = int(input("Specify a day of the month: "))
    
    computeOrdinalDate(year, month, day)

if __name__ == "__main__":
    main()
