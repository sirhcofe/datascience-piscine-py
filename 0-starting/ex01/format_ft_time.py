import time
import datetime

current_time = time.time()

print("Seconds since January 1, 1970: {0:,.6f} or {1:.2e} in scientific notation".format(current_time, current_time))

current_datetime = datetime.datetime.now()
format_date = current_datetime.strftime("%b %d %Y")

print(format_date)