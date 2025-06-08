#- Calculate the days between two dates
import datetime
## Enter your dates here in YYYY-MM-DD format
date1_str ="2023, 10, 1"
date2_str ="2025, 5, 25"
# Convert the string dates to datetime objects
date1 = datetime.datetime.strptime(date1_str, "%Y, %m, %d")
date2 = datetime.datetime.strptime(date2_str, "%Y, %m, %d")
# Calculate the difference between the two dates    
date_difference = abs((date2 - date1).days)
print("Number of days between the two dates:",date_difference)

