import json
from requests import Response
import requests
from datetime import datetime
import random
import string


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]
    
    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Cannot find header with name {header_name} in the last response"
        return response.headers[header_name]
    
    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        
        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        return response_as_dict[name]
    
    def prepare_registration_data(self, email=None, username=None, firstName=None, lastName=None, password=None):
        if email is None:
            basepart = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{basepart}{random_part}@{domain}"
        
        if username is None:
            username = 'learnqa'
        
        if firstName is None:
            firstName = 'learnqa'
        
        if lastName is None:
            lastName = 'learnqa'
        
        if password is None:
            password = '123'

        # if email is None:
        #     random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        #     email = f"learnqa{random_part}@example.com"
            
        return {
            'password': password,
            'username': username,
            'firstName': firstName,
            'lastName': lastName,
            'email': email
        }
    
