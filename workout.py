import random


# Added argument 'num_activities' to make the choices dynamically
# Function to generate a workout plan with a specified number of activities
def generate_workout_plan(num_activities):
    workouts = [
        "Push-ups",
        "Sit-ups",
        "Squats",
        "Jumping Jacks",
        "Running",
        "Cycling",
        "Swimming",
        "Yoga",
    ]
    workout_plan = []

    # deleted '5'and added argument to make the choices dynamically
    # Generate a workout plan with the specified number of activities
    for i in range(num_activities):
        workout_plan.append(random.choice(workouts))

    return workout_plan
# testing/debugging:
# num_activities = int(input("Enter the number of activities you want in your workout plan: "))
# workout_plan = generate_workout_plan(num_activities)
# print(workout_plan)
