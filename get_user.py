import requests

resp = requests.get("https://reqres.in/api/users?page=2")
# print(resp.status_code)

print(resp.json())
json_response = resp.json()
print(json_response['total'])
print(json_response['total_pages'])
print(json_response['data'][0]['email'])
print(json_response["data"][0]["email"].endswith("reqres.in"))
print(json_response["data"][2]["last_name"])
print(json_response["support"]["url"])