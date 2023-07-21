import auth
import calories
import log
import progress
import workout

# Moved 'progress' and 'burned_calories' to 'progress.py'

def main():
    # Authenticate the user before proceeding
    if auth.authenticate_user():
        # Prompt the user to enter the number of activities in the workout plan
        num_activities = int(
            input("Enter the number of activities you want in your workout plan: "))
        workout_plan = workout.generate_workout_plan(num_activities)
        total_calories_burned = 0

        for activity in workout_plan:
            # Calculate calories burned and duration for each activity
            calories_burned, duration = calories.calculate_calories_burned(
                activity)
            # Log the activity details to "activity_log.txt" file
            log.log_activity(activity, calories_burned,
                             progress.get_workout_count(), duration)
            # Update the progress for the activity
            progress.update_progress(activity)
            total_calories_burned += calories_burned
        # Display the results to the user
        print()
        print("====WELL DONE!====")
        print("****YOUR RESULTS:")
        print(f"You have completed {progress.get_workout_count()} workouts.")
        print(f"You have burned {total_calories_burned} calories today.")
        print(f"You have completed {progress.get_progress()}% of your goal.")
        print()


if __name__ == "__main__":
    main()
