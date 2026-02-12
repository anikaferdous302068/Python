import datetime

# Loop through months 1 to 12
for month in range(1, 13):
    # Create a date object (year and day can be anything valid)
    date_obj = datetime.date(2024, month, 1)
    
    # Print full month name
    print(date_obj.strftime("%B"))