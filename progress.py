# Added progress dictionary to track progress of different workouts
progress = {
    "Running": 0,
    "Cycling": 0,
    "Swimming": 0,
    "Yoga": 0,
    "Push-ups": 0,
    "Sit-ups": 0,
    "Squats": 0,
    "Jumping Jacks": 0,
}
# Added burned_calories dictionary to track burned calories for different workouts
burned_calories = {
    "Running": 0,
    "Cycling": 0,
    "Swimming": 0,
    "Yoga": 0,
    "Push-ups": 0,
    "Sit-ups": 0,
    "Squats": 0,
    "Jumping Jacks": 0,
}
# Function to update progress dictionary


def update_progress(workout):
    progress[workout] += 1

# Function to get the total number of completed workouts


def get_workout_count():
    return sum(progress.values())

# Function to get the progress percentage


def get_progress():
    total_workouts = len(progress)
    if total_workouts == 0:
        return 0
    total_completed = sum(progress.values())
    return (total_completed / (total_workouts * 5)) * 100


# Test the function by updating the progress for different workouts
# update_progress(progress_dict, "Push-ups")
# update_progress(progress_dict, "Jumping Jacks")
# update_progress(progress_dict, "Squats")
# update_progress(progress_dict, "Push-ups")
# update_progress(progress_dict, "Sit-ups")

# Print the updated progress:
# print("Updated Progress: ")
# for workout, count in progress.items():
    # print(f"{workout}: {count} times")
