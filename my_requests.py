import requests

def get_random_activities(num_activities):
    url = "https://www.boredapi.com/api/activity/"
    params = {"participants": 1}  # Specify the number of participants for each activity
    activities = []
    for _ in range(num_activities):
        response = requests.get(url, params=params)
        data = response.json()
        activity = data["activity"]
        activities.append(activity)
    return activities

# Get user input for the number of activities
while True:
    try:
        num_activities = int(input("Enter the number of activities to generate: "))
        break
    except ValueError:
        print("Please enter a valid number.")

activities = get_random_activities(num_activities)
for i, activity in enumerate(activities, start=1):
    print(f"Activity {i}: {activity}")
