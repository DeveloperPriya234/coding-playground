year = 2025

if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,"is a leap year")
else:
    print(year,"IS NOT A LEAP YEAR")