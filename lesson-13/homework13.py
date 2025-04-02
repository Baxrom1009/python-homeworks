from datetime import datetime, timedelta
import re
import pytz
import time

# Age Calculator
def calculate_age():
    birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
    today = datetime.today()
    age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    age_months = today.month - birth_date.month if today.month >= birth_date.month else (12 + today.month - birth_date.month)
    age_days = (today - birth_date).days % 30
    print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")

# Days Until Next Birthday
def days_until_birthday():
    birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d").replace(year=datetime.today().year)
    if birth_date < datetime.today():
        birth_date = birth_date.replace(year=birth_date.year + 1)
    days_left = (birth_date - datetime.today()).days
    print(f"Your next birthday is in {days_left} days.")

# Meeting Scheduler
def meeting_scheduler():
    current_datetime = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    duration_hours = int(input("Enter meeting duration (hours): "))
    duration_minutes = int(input("Enter meeting duration (minutes): "))
    current_datetime = datetime.strptime(current_datetime, "%Y-%m-%d %H:%M")
    end_time = current_datetime + timedelta(hours=duration_hours, minutes=duration_minutes)
    print(f"The meeting will end at: {end_time.strftime('%Y-%m-%d %H:%M')}")

# Timezone Converter
def timezone_converter():
    date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_tz = input("Enter your current timezone (e.g., UTC, US/Eastern): ")
    to_tz = input("Enter the target timezone: ")
    dt_obj = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    localized_dt = from_zone.localize(dt_obj)
    converted_dt = localized_dt.astimezone(to_zone)
    print(f"Converted time: {converted_dt.strftime('%Y-%m-%d %H:%M %Z')}")

# Countdown Timer
def countdown_timer():
    future_time = input("Enter future date and time (YYYY-MM-DD HH:MM): ")
    future_time = datetime.strptime(future_time, "%Y-%m-%d %H:%M")
    while True:
        remaining = future_time - datetime.now()
        if remaining.total_seconds() <= 0:
            print("Time's up!")
            break
        print(f"Time remaining: {remaining}", end="\r")
        time.sleep(1)

# Email Validator
def email_validator():
    email = input("Enter an email address: ")
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    print("Valid Email" if re.match(pattern, email) else "Invalid Email")

# Phone Number Formatter
def phone_formatter():
    phone = input("Enter a 10-digit phone number: ")
    formatted_phone = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print(f"Formatted Number: {formatted_phone}")

# Password Strength Checker
def password_strength_checker():
    password = input("Enter a password: ")
    if (len(password) >= 8 and any(c.isupper() for c in password) and
            any(c.islower() for c in password) and any(c.isdigit() for c in password)):
        print("Strong password")
    else:
        print("Weak password")

# Word Finder
def word_finder():
    text = input("Enter a text: ")
    word = input("Enter the word to find: ")
    occurrences = [m.start() for m in re.finditer(rf'\b{word}\b', text)]
    print(f"Occurrences found at positions: {occurrences}")

# Date Extractor
def date_extractor():
    text = input("Enter text: ")
    dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
    print(f"Extracted Dates: {dates}")

# Menu
def main():
    functions = {
        "1": calculate_age,
        "2": days_until_birthday,
        "3": meeting_scheduler,
        "4": timezone_converter,
        "5": countdown_timer,
        "6": email_validator,
        "7": phone_formatter,
        "8": password_strength_checker,
        "9": word_finder,
        "10": date_extractor
    }
    while True:
        print("\nChoose an option:")
        print("1. Age Calculator")
        print("2. Days Until Next Birthday")
        print("3. Meeting Scheduler")
        print("4. Timezone Converter")
        print("5. Countdown Timer")
        print("6. Email Validator")
        print("7. Phone Number Formatter")
        print("8. Password Strength Checker")
        print("9. Word Finder")
        print("10. Date Extractor")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "0":
            break
        elif choice in functions:
            functions[choice]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
