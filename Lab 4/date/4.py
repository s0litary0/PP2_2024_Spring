import datetime

x = datetime.datetime.now()
y = datetime.datetime(2023, 2, 19)

print("Difference:", abs(x.year - y.year) * 52 * 7 * 24 * 60 * 60 +
 abs(x.month - y.month) * 30 * 24 * 60 * 60 + 
 abs(x.day - y.day) * 24 * 60 * 60)