import requests
import pytest

def test_identify_cookie():
    response = requests.get('https://playground.learnqa.ru/api/homework_cookie')

    assert response.status_code == 200

    cookies = response.cookies.get_dict()

    print(f"Cookies:{cookies}")

    assert cookies, "No cookies received"

    assert 'HomeWork' in cookies, "Cookie 'HomeWork' is absent"

    print("Value of 'HomeWork' cookie:", cookies['HomeWork'])

    expected_cookie_value = 'hw_value'  

    assert cookies['HomeWork'] == expected_cookie_value, f"Expected 'HomeWork' cookie value is '{expected_cookie_value}'"