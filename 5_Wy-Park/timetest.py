from datetime import datetime, date
import time

date_time1 = datetime.now()

print(f"date_time1 = {date_time1}")

time.sleep(5)

date_time2 = datetime.now()

print(f"date_time2 = {date_time2}")

if date_time1 < date_time2:
    print(f"date_time1 is less than date_time2")
else:
    print("Fail")
