'''
Project Euler Problem 19

How many sundays fell on the first of the month during
the twentieth century, 1 Jan, 1901 - 31 Dec 2000?
'''

#number of days per month, feb is a special case tho
days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
weekday = 1 #1 Jan 1900 was a monday
current_month = 1 #start in January
current_day = 1 #on the 1st
year = 1900
hits = 0 #hit is when we get a sunday on the 1st

while year < 2000:
	print year, current_month, current_day
	if current_day < days_in_month[current_month]:
		current_day += 1
	else:
		if not current_month == 2:
			current_day = 1
			if current_month < 12:
				current_month += 1
			else:
				year += 1
				current_month = 1
		else:
			if current_day == 28:
				if not year % 4:
					current_day += 1
				else:
					current_day = 1
					current_month = 3
			elif current_day == 29:
				current_day = 1
				current_month = 3
	weekday += 1
	if weekday == 7:
		if current_day == 1:
			hits += 1
			#print year, current_month, current_day, weekday
		weekday = 0

print hits
