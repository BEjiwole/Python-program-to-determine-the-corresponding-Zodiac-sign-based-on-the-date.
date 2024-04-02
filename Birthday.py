import pandas as pd
from datetime import datetime

# Function to determine Zodiac sign based on birthdate
def zodiac_sign(birthdate):
    month, day = birthdate.month, birthdate.day
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    # Add other Zodiac signs here
    else:
        return "Unknown"

# Prompt user for input
name = input("Enter the name of the person: ")
birthdate_str = input("Enter the birthdate (YYYY-MM-DD): ")

# Convert birthdate string to datetime object
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

# Determine Zodiac sign
sign = zodiac_sign(birthdate)

# Create DataFrame
data = {'Name': [name], 'Birthdate': [birthdate_str], 'Zodiac Sign': [sign]}
df = pd.DataFrame(data)

# Save data to CSV file
df.to_csv('zodiac_signs.csv', index=False)
