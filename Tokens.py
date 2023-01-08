import requests, time, json
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.text, response.status_code)
obj = json.loads(response.text)
key = "token"
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":obj[key]})
print(response.text, response.status_code)
sec = "seconds"
print('Ждем ',obj[sec])
time.sleep(obj[sec])
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":obj[key]})
print(response.text, response.status_code)
obj = json.loads(response.text)
key1 = "result"
key2="status"
if key1 in obj:
    if obj[key2]=="Job is ready":
        print("Задача готова")
else:
    print(f"Ключа {key1} в JSON нет")