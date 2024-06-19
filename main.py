import requests
import pprint
# response = requests.get('https://api.github.com')
# response_json = response.json()
# # print(response.status_code)
# # print(response.ok)
# #
# # if response.ok:
# #     print("запрос выполнен успешно")
# # else:
# #     print("запрос не выполнен")
#
# print(response_json)
# pprint.pprint(response_json)
#
# params = {
#     'q': 'python'
# }
# responce = requests.get('https://api.github.com/search/repositories', params=params)
# responce_json = responce.json()
# #pprint.pprint(responce_json)
# print(f"Количество репозиториев python', {responce_json['total_count']}")

# img = "https://tastyseason.ru/distributor/"
# responce = requests.get(img)
#
# with open ('image.jpeg', 'wb') as file:
#     file.write(responce.content)

# response = requests.get('https://google.com')
# print(response.status_code)
# print(response.ok)
# print(response.headers)
# print(response.text)

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     'title': 'тестовый пост запрос',
#     'body': 'тестовый контент пост запроса',
#     'userId': 2
# }
# response = requests.post(url, data=data)
# print(response.status_code)
# print(f"ответ сервера: {response.json()}")
