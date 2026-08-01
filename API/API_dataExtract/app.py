import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)

data = response.json()

# print(data)

# print(type(data))

# print(data[0])

for user in data:
    print(user["name"])