import requests
#4 вопрос
print("Четвертый вопрос")
k=['GET','POST','PUT','DELETE']
print("Метод POST")
for i in k:
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":i})
    print(response.text, response.status_code,i)
print("Метод PUT")
for i in k:
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":i})
    print(response.text, response.status_code,i)
print("Метод DELETE")
for i in k:
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":i})
    print(response.text, response.status_code,i)
print("Метод GET")
for i in k:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":i})
    print(response.text, response.status_code,i)