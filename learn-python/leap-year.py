def is_leap(year):
    if ((year%4 == 0) and ((year%100 != 0) or (year%400 == 0))):
        return True
    else:
        return False   


year = int(input('Enter a year to know whether it is a leap year or not ??  '))
print(is_leap(year))