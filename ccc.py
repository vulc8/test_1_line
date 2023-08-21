import requests




def dd(num) :
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer wg8uJ5eUZ1LjzxIAcp9kmZgdVtpJs8PihTKqzXZDRcH"
    }
    data = {
        "message":num
    }

for i in range(1, 11) :
    dd(i)