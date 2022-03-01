from datetime import date, timedelta
 
today = date.today()
print("Today: ", today)
 
cnt = timedelta(1)

print("Tomorrow: ", today + cnt)

cnt2 = timedelta(-1)

print("Yesterday: ", today + cnt2)
