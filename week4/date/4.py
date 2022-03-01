
 
from datetime import datetime
 
string = str(input('First date: '))
date = datetime.strptime(string, "%Y-%m-%d %H:%M")
string2 = str(input('Second date: '))
date2 = datetime.strptime(string2, "%Y-%m-%d %H:%M")
 
print(abs((date2 - date).total_seconds()))