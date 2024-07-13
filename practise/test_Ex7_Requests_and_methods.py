import requests
import requests.cookies
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"


#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.


response_get = requests.get(url)
if response_get.status_code == 200:
    print(f"GET without method:{response_get.text}")
else:
    print(f"GET request failed with status code: {response_get.status_code}")


response_post = requests.post(url)
if response_post.status_code == 200:
    print(f"POST without method:{response_post.text}")
else:
    print(f"POST request failed with status code: {response_get.status_code}")


response_put = requests.put(url)
if response_put.status_code == 200:
    print(f"PUT without method:{response_put.text}")
else:
    print(f"PUT request failed with status code: {response_get.status_code}")


response_delete = requests.delete(url)
if response_delete.status_code == 200:
    print(f"DELETE without method:{response_delete.text}")
else:
    print(f"DELETE request failed with status code: {response_delete.status_code}")


#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае. 

response_head = requests.head(url)
if response_head.status_code == 200:
    print(f"HEAD method:{response_head.text}")
else:
    print(f"HEAD request failed with status code: {response_head.status_code}")



#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.

payload = {"method": "GET"}
response_get = requests.get(url,params=payload )

if response_get.status_code == 200:
    print(f"GET with method GET:{response_get.text}")
else:
    print(f"GET with method GET request failed with status code: {response_get.status_code}")

payload = {"method": "POST"}
response_post = requests.post(url, data = payload)
if response_post.status_code == 200:
    print(f"POST with method POST:{response_post.text}")
else:
    print(f"POST with meethod POST request failed with status code: {response_get.status_code}")

payload = {"method": "PUT"}
response_put = requests.put(url, data = payload)
if response_put.status_code == 200:
    print(f"PUT with method PUT:{response_put.text}")
else:
    print(f"PUT with method PUT request failed with status code: {response_get.status_code}")

payload = {"method": "DELETE"}
response_delete = requests.delete(url, data = payload)
if response_delete.status_code == 200:
    print(f"DELETE with method DELETE:{response_delete.text}")
else:
    print(f"DELETE with DELETE request failed with status code: {response_delete.status_code}")

#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

methods = ["GET", "POST", "PUT", "DELETE"]

for method in methods:
    for param_method in methods:
        try: 
            if method == "GET":
                response = requests.get(url, params={"method": param_method})
            else:
                response = requests.request(method, url, data={"method": param_method})
            
            if response.status_code == 200:
                if method != param_method:
                    print(f"NOT identical method and param: method={method}, param ={param_method}, Status code={response.status_code}, Response text: {response.text}")
                else:
                    print(f"IDENTICAL method and param: method={method}, param ={param_method}, Status code={response.status_code}, Response text: {response.text}")
        except Exception as e:
            print(f"Error occured:{TypeError},Error message:{e}, method={method}, Param method={param_method}, Status code={response.status_code}, Response text: {response.text}")