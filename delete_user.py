import requests

resp = requests.delete("https://reqres.in/api/users/2")
print(resp.status_code)