#import calendar 
#print(calendar.calendar(2025))
#print(calendar.month(2024,7))
#print(calendar.isleap(2025))
from datetime import datetime
a=input("enter first date(YYYY-MM-DD):")
b=input("enter second date(YYYY-MM-DD):")

d1=datetime.strptime(a,"%Y-%m-%d")
d2=datetime.strptime(b,"%Y-%m-%d")
diff=d2-d1
print("Difference", abs(diff.days),"days")

