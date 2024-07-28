import requests
import allure
from base.base_case import BaseCase
from base.assertions import Assertions

@allure.epic("User Management")
@allure.feature("User Edit")
class TestUserEdit(BaseCase):

    @allure.story("Edit Just Created User")
    @allure.description("This test registers a new user, logs in, edits their first name, and verifies the change.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_just_created_user(self):
        with allure.step("Register a new user"):
            register_data = self.prepare_registration_data()
            response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")

            email = register_data['email']
            first_name = register_data['firstName']
            password = register_data['password']
            user_id = self.get_json_value(response1, "id")

        with allure.step("Login as the newly created user"):
            login_data = {'email': email, 'password': password}
            response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step("Edit the user's first name"):
            new_name = "Changed_Name"
            response3 = requests.put(
                f"https://playground.learnqa.ru/api/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
                data={"firstName": new_name}
            )
            Assertions.assert_code_status(response3, 200)

        with allure.step("Get the user data and verify the first name has been changed"):
            response4 = requests.get(
                f"https://playground.learnqa.ru/api/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid}
            )
            Assertions.assert_json_value_by_name(
                response4,
                "firstName",
                new_name,
                "Wrong name after user name editing"
            )

    @allure.story("Edit User Without Authentication")
    @allure.description("This test tries to edit a user without being authenticated and expects a 400 error.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_user_not_auth(self):
        with allure.step("Register a new user"):
            register_data = self.prepare_registration_data()
            response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")
            user_id = self.get_json_value(response1, "id")

        with allure.step("Attempt to edit the user without authentication"):
            new_name = "Changed_Name"
            response3 = requests.put(
                f"https://playground.learnqa.ru/api/user/{user_id}",
                data={"firstName": new_name}
            )
            Assertions.assert_code_status(response3, 400)

    @allure.story("Edit User Authenticated as Another User")
    @allure.description("This test registers two users and tries to edit the first user while authenticated as the second user.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_user_auth_as_another_user(self):
        with allure.step("Register the first user"):
            register_data = self.prepare_registration_data()
            response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")
            user_id = self.get_json_value(response1, "id")

        with allure.step("Register the second user"):
            register_data2 = self.prepare_registration_data()
            response2 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data2)
            Assertions.assert_code_status(response2, 200)
            Assertions.assert_json_has_key(response2, "id")
            email = register_data2['email']
            password = register_data2['password']

        with allure.step("Login as the second user"):
            login_data = {'email': email, 'password': password}
            response3 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
            auth_sid = self.get_cookie(response3, "auth_sid")
            token = self.get_header(response3, "x-csrf-token")

        with allure.step("Attempt to edit the first user while logged in as the second user"):
            new_name = "Changed_Name"
            response4 = requests.put(
                f"https://playground.learnqa.ru/api/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
                data={"firstName": new_name}
            )
            Assertions.assert_code_status(response4, 400)

    @allure.story("Edit User Email Without '@'")
    @allure.description("This test tries to edit a user's email to an invalid email without '@' and expects a 400 error.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_user_email_without_at(self):
        with allure.step("Register a new user"):
            register_data = self.prepare_registration_data()
            response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")
            email = register_data['email']
            password = register_data['password']
            user_id = self.get_json_value(response1, "id")

        with allure.step("Login as the newly created user"):
            login_data = {'email': email, 'password': password}
            response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step("Attempt to edit the user's email to an invalid email"):
            new_email = "newemail.com"
            response3 = requests.put(
                f"https://playground.learnqa.ru/api/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
                data={"email": new_email}
            )
            Assertions.assert_code_status(response3, 400)

    @allure.story("Edit User First Name Too Short")
    @allure.description("This test tries to edit a user's first name to a single character and expects a 400 error.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_user_first_name_too_short(self):
        with allure.step("Register a new user"):
            register_data = self.prepare_registration_data()
            response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")
            email = register_data['email']
            password = register_data['password']
            user_id = self.get_json_value(response1, "id")

        with allure.step("Login as the newly created user"):
            login_data = {'email': email, 'password': password}
            response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step("Attempt to edit the user's first name to a single character"):
            new_name = "a"
            response3 = requests.put(
                f"https://playground.learnqa.ru/api/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
                data={"firstName": new_name}
            )
            Assertions.assert_code_status(response3, 400)