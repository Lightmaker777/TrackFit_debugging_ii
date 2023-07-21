# Fixed issue and made sure that the activities are appended("a") to the file instead of overwriting("w") it.
# Function to get the progress percentage

def log_activity(activity, calories_burned, num_workouts, duration):
    with open("activity_log.txt", "a") as file:
        file.write(f"Activity: {activity}\n")
        file.write(f"Calories Burned: {calories_burned} calories\n")
        file.write(f"Number of Workouts: {num_workouts + 1}\n")
        file.write(f"Duration: {duration} minutes\n\n")


# testing the function:
# log_activity("Push-ups")
# log_activity("Jumping Jacks")
# log_activity("Squats")
