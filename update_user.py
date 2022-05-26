import requests

payload = {
    "name": "API",
    "job": "API testing"
}
resp = requests.put("https://reqres.in/api/users/2", data=payload)
print(resp)
print(resp.json())
print(resp.json()['job'] == "API testing")
