from datetime import date

def calculate_age(day, month, year):
    today = date.today()
    dob = date(year, month, day)
    age_years = today.year - dob.year

    # Check if birthday has not occurred yet this year
    if (today.month, today.day) < (dob.month, dob.day):
        age_years -= 1

    print("Your age is:", age_years, "years")

# Example usage
d = int(input("Enter Day of Birth: "))
m = int(input("Enter Month of Birth: "))
y = int(input("Enter Year of Birth: "))