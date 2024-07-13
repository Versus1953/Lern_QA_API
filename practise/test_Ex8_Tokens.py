import requests
import time

# URL API метода
url = "https://playground.learnqa.ru/ajax/api/longtime_job"

# 1) создавал задачу
response = requests.get(url)
print(response.text)
try:
    if response.status_code == 200:
        resonse_json = response.json()
        seconds = resonse_json["seconds"]
        token = resonse_json["token"]
        print(f"The task has been created. Awaiting time: {seconds} seconds. Token: {token}")
except Exception as e:
    print(f"The task hasn't been created. Erorr occured {e}")


# 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
response = requests.get(url, params={"token": token})
try:
    if response.status_code == 200:
        status_data = response.json()
        if status_data["status"] == "Job is NOT ready":
            print("Job is NOT ready.")
        else:
            print("Current task status:", status_data)
except Exception as e:
    print("Error occured with status check up")


# 3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
time.sleep(seconds)


# 4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
response = requests.get(url, params={"token": token})
print(response.text)
try:
    if response.status_code == 200:
        status_data = response.json()
        if status_data["status"] == "Job is ready" and "result" in status_data:
            print("The task completed. Result:", status_data["result"])
        else:
            print("Unexpected outcome:", status_data)
except Exception as e:
    print("Error occured with status compliting")