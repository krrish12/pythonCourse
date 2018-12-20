import calendar

print(calendar.calendar(2018,1,3,10))#syntax year,width,column space, number of lines
#output: calendar

print(calendar.firstweekday())
#output: 0

print(calendar.isleap(2018))
#output: False

print(calendar.leapdays(2010,2018))
#output: 2
#number of leaf days between two years

print(calendar.month(2018,12,1,1))#syntax year,month,width, number of lines
#output: print given month

print(calendar.monthcalendar(2018,12))
#output: [[0, 0, 0, 0, 0, 1, 2], [3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30], [31, 0, 0, 0, 0, 0, 0]]
#list of integers

print(calendar.monthrange(2018,12))
# returns two integer 1st result is 1st day of given month and 2nd result is number of days in given month

print(calendar.weekday(2018,12,17))
#output: returns the weekday code for given data 0 as Monday and 6 as Sunday

print(calendar.prcal(2018))
#ouput: print calendar of given year with autofit
