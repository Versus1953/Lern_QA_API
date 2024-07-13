import requests
import pytest

def test_identify_header():
    response = requests.get('https://playground.learnqa.ru/api/homework_header')

    assert response.status_code == 200

    headers = response.headers

    assert headers, "No headers were received"

    for header_name, header_value in headers.items():
        print(f"{header_name}: {header_value}")

    expected_header_name = 'x-secret-homework-header' 

    expected_header_value = 'Some secret valu'  

    assert expected_header_name in headers, f"Header: {expected_header_name} is absent"

    assert headers[expected_header_name] == expected_header_value, f"Unexpected header's value {headers[expected_header_name]}"

    