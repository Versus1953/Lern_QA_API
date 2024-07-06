import requests

url = 'https://playground.learnqa.ru/api/long_redirect'
response = requests.get(url)

redirect_count = len(response.history)
final_url = response.url

print(f'Redirect count: {redirect_count}')
print(f'Final URL: {final_url}')