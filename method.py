import requests
#1 вопрос
print(f"Первый вопрос: четыре метода вызываются последовательно, без параметра")
response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
response2 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
response4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response1.text, response1.status_code)
print(response2.text,response2.status_code)
print(response3.text, response3.status_code)
print(response4.text, response4.status_code)
#2 вопрос
print(f"Второй вопрос: посылаю метод не из списка:PATCH")
response5 = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response5.text, response5.status_code)
#3 вопрос
print(f"Третий вопрос")
response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
response2 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"POST"})
response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"PUT"})
response4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"DELETE"})
print(response1.text, response1.status_code)
print(response2.text,response2.status_code)
print(response3.text, response3.status_code)
print(response4.text, response4.status_code)


