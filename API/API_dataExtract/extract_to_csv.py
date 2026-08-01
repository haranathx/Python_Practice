import requests
import csv

# API URL
url = "https://jsonplaceholder.typicode.com/users"

print("Connecting to API...")

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    print("Connected Successfully!")

    # Convert JSON to Python object
    users = response.json()

    # Create CSV file
    with open("users.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # CSV Header
        writer.writerow([
            "ID",
            "Name",
            "Username",
            "Email",
            "Phone",
            "Website",
            "Company",
            "City"
        ])

        # Write each user's data
        for user in users:
            writer.writerow([
                user["id"],
                user["name"],
                user["username"],
                user["email"],
                user["phone"],
                user["website"],
                user["company"]["name"],
                user["address"]["city"]
            ])

    print("Data saved successfully to users.csv")

else:
    print("API Error:", response.status_code)