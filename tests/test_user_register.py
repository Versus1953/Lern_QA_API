import requests
import pytest
import allure
from base.base_case import BaseCase
from base.assertions import Assertions
import random
import string


@allure.epic("User Management")
@allure.feature("User Registration")
class TestUserRegister(BaseCase):

    @allure.story("Create User Successfully")
    @allure.description("This test registers a new user and expects a successful response with a user ID.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_successfully(self):
        with allure.step("Prepare registration data"):
            data = self.prepare_registration_data()
        
        with allure.step("Send POST request to create user"):
            response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
            print(f'Check id: {response}')

        with allure.step("Assert response status code and presence of user ID"):
            Assertions.assert_code_status(response, 200)
            Assertions.assert_json_has_key(response, "id")

    @allure.story("Create User with Existing Email")
    @allure.description("This test tries to register a user with an email that already exists and expects a 400 response.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        with allure.step("Prepare registration data with existing email"):
            data = self.prepare_registration_data(email=email) 
        
        with allure.step("Send POST request to create user"):
            response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        with allure.step("Assert response status code and error message"):
            Assertions.assert_code_status(response, 400)
            assert response.text == f"Users with email '{email}' already exists", f"Unexpected response content: {response.text}"

            print(response.status_code)
            print(response.text)

    @allure.story("Create User with Incorrect Email")
    @allure.description("This test tries to register a user with an incorrect email format and expects a 400 response.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_incorrect_email(self):
        email = 'vinkotov.example.com'
        with allure.step("Prepare registration data with incorrect email"):
            data = self.prepare_registration_data(email=email)
        
        with allure.step("Send POST request to create user"):
            response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
            print(response.content)

        with allure.step("Assert response status code and error message"):
            Assertions.assert_code_status(response, 400)
            assert response.text == "Invalid email format", f"Unexpected response content: {response.text}"

    @allure.story("Create User Without Required Field")
    @allure.description("This test tries to register a user without one of the required fields and expects a 400 response.")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("missed_field", ["username", "email", "firstName", "lastName", "password"])
    def test_create_user_without_field(self, missed_field):
        with allure.step(f"Prepare registration data without field {missed_field}"):
            data = {key: value for key, value in self.prepare_registration_data().items() if key != missed_field}
        
        with allure.step("Send POST request to create user"):
            response = requests.post('https://playground.learnqa.ru/api/user/', data=data)
            print(response.content)

        with allure.step("Assert response status code and error message"):
            Assertions.assert_code_status(response, 400) 
            expected_error_message = f"The following required params are missed: {missed_field}"
            assert response.text == expected_error_message, f"Unexpected response content: {response.text}"

    @allure.story("Create User with Short First Name")
    @allure.description("This test tries to register a user with a first name that is too short and expects a 400 response.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_short_name(self):
        with allure.step("Prepare registration data with short first name"):
            data = self.prepare_registration_data(firstName='a')
        
        with allure.step("Send POST request to create user"):
            response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        with allure.step("Assert response status code and error message"):
            Assertions.assert_code_status(response, 400)
            assert response.text == "The value of 'firstName' field is too short", f"Unexpected response content: {response.text}"

    @allure.story("Create User with Long First Name")
    @allure.description("This test tries to register a user with a first name that is too long and expects a 400 response.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_long_name(self):
        with allure.step("Generate a long first name"):
            long_name = ''.join(random.choice(string.ascii_letters) for _ in range(251))
        
        with allure.step("Prepare registration data with long first name"):
            data = self.prepare_registration_data(firstName=long_name)
        
        with allure.step("Send POST request to create user"):
            response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        with allure.step("Assert response status code and error message"):
            Assertions.assert_code_status(response, 400)
            assert response.text == "The value of 'firstName' field is too long", f"Unexpected response content: {response.text}"