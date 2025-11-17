from datetime import date, datetime, timedelta

today = date.today()
print(today)


now = datetime.now()
print(now)

# Format as "YYYY-MM-DD HH:MM:SS"
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted datetime: {formatted_datetime}")

# Format as "DayName, MonthName Day, Year"
formatted_date_textual = now.strftime("%A, %B %d, %Y")
print(f"Textual date: {formatted_date_textual}")

# Format as "DD/MM/YYYY"
formatted_date_short = now.strftime("%d/%m/%Y")
print(f"Short date: {formatted_date_short}")



today = date.today()

# Add days
future_date = today + timedelta(days=30)
print(f"Date 30 days from now: {future_date}")

# Subtract days
past_date = today - timedelta(days=30)
print(f"Date 30 days ago: {past_date}")

# Modify specific components (year, month, day) using replace()
modified_date = today.replace(year=2026, month=4, day=1)
print(f"Modified date (April 1, 2026): {modified_date}")




