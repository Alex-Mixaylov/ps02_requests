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

params = {
    'q': 'python'
}
responce = requests.get('https://api.github.com/search/repositories', params=params)
responce_json = responce.json()
#pprint.pprint(responce_json)
print(f"Количество репозиториев python', {responce_json['total_count']}")