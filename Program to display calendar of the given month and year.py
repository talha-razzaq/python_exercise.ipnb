#Program to display calendar of the given month and year

#import calendar
import calendar

#take user input
yy = int(input("Enter the year : "))
mm = int(input("Enter the month : "))


#display calendar
print(calendar.month(yy, mm))