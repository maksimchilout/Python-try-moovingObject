from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta


one = None
two = None
a = input("pre")
if a:
    one = datetime.now()
    print(one)

b = input("adsa")
if b:
    two = (datetime.now()).time()

c = input("dsas")
if c:
    d = datetime.now() - one
    print(d)
    print(date.today())
    to_dict = dict(date = str(date.today()), time= str(d))
    print(to_dict)
