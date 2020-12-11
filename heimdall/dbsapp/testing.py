import requests

MAIN_URL2 = "https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/accounts/view"
result2 = requests.post(MAIN_URL2, headers={"x-api-key":"1elJCmVDjP45as0PT9fsEmHvP03074O8h05lQUmh"}, json={"custID":8})
print(result2.status_code)
