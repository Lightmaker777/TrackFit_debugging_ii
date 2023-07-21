import datetime

# Function to calculate the duration in minutes between start and end times


def get_duration_in_minutes(start_time, end_time):
    fmt = "%H:%M"  # Define the time format
    # added .datetime that Lisa forgotten to add
    # try except to handle the exception that Lisa forgot to handle
    try:
        start = datetime.datetime.strptime(start_time, fmt)
        # added .datetime that Lisa forgotten to add
        end = datetime.datetime.strptime(end_time, fmt)
        duration = end - start
        # added .total_seconds() that Lisa forgot to add
        duration_minutes = duration.total_seconds() // 60
        return int(duration_minutes)
    except ValueError:
        print("Incorrect time format, should be HH:MM")
        return 0

# Function to calculate the calories burned for an activity based on its duration


def calculate_calories_burned(activity):
    calorie_chart = {
        "Running": 600,
        "Cycling": 500,
        "Swimming": 700,
        "Yoga": 300,
        "Push-ups": 300,
        "Sit-ups": 500,
        "Squats": 300,
        "Jumping Jacks": 700,
    }
    start_time = input(f"\nEnter the start time for {activity} (HH:MM): ")
    end_time = input(f"Enter the end time for {activity} (HH:MM): ")

    duration_minutes = get_duration_in_minutes(
        start_time, end_time)  # removed '// 30'

# added condition to check if the activity is in the calorie chart
    if activity in calorie_chart:
        calories_per_hour = calorie_chart[activity]
        calories_burned = (calories_per_hour * duration_minutes) // 60
        return calories_burned, duration_minutes
    else:
        print("Activity not found in the calorie chart.")
        return 0, 0

# Test the function
# activity = input("Enter the activity you performed: ")
# calories_burned = calculate_calories_burned(activity)
# print(f"Calories burned: {calories_burned} calories")
