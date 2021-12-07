from datetime import datetime

mydate = datetime(2019, 12, 31, 23, 59, 59)
print(mydate)
mydate = mydate.replace(year=2020)
print(mydate)