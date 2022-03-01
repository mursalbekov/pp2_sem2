from datetime import date, timedelta

n = 1
 
today = date.today()
 
print("Today: ", today)
for i in range(0, 5):
	cnt = timedelta(i)
	print("After ", end = '')
	print(n, end = ' ')
	n = n + 1
	print( "days date will be: ", today + cnt)