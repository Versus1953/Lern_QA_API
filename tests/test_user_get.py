import requests
import allure
from base.base_case import BaseCase
from base.assertions import Assertions
from base.my_requests import MyRequests

@allure.epic("User Management")
@allure.feature("User Details")
class TestUserGet(BaseCase):

    @allure.story("Get User Details Without Authentication")
    @allure.description("This test checks that a non-authenticated user can only see the username of another user.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_details_not_auth(self):
        with allure.step("Get user details without authentication"):
            response = MyRequests.get("/user/2")
            print(response.content)
        
        with allure.step("Verify response contains 'username' and does not contain 'email', 'firstName', 'lastName'"):
            Assertions.assert_json_has_key(response, "username")
            Assertions.assert_json_has_not_key(response, "email")
            Assertions.assert_json_has_not_key(response, "firstName")
            Assertions.assert_json_has_not_key(response, "lastName")

    @allure.story("Get User Details Authenticated as Same User")
    @allure.description("This test checks that an authenticated user can see their own details.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_user_details_auth_as_same_user(self):
        with allure.step("Login with valid credentials"):
            data = {
                "email": "vinkotov@example.com",
                "password": "1234"
            }
            response1 = MyRequests.post("/user/login", data=data)
            print(response1.content)
        
        with allure.step("Extract auth_sid, token, and user_id from login response"):
            auth_sid = self.get_cookie(response1, "auth_sid")
            token = self.get_header(response1, "x-csrf-token")
            user_id_from_auth_method = self.get_json_value(response1, 'user_id')

        with allure.step("Get user details authenticated as same user"):
            headers = {"x-csrf-token": token}
            cookies = {"auth_sid": auth_sid}
            response2 = MyRequests.get(f"/user/{user_id_from_auth_method}", headers=headers, cookies=cookies)
            print(response2.content)

        with allure.step("Verify response contains 'username', 'email', 'firstName', 'lastName'"):
            expected_fields = ["username", "email", "firstName", "lastName"]
            Assertions.assert_json_has_keys(response2, expected_fields)

    @allure.story("Get User Details Authenticated as Another User")
    @allure.description("This test checks that an authenticated user can only see the username of another user.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user_details_auth_as_another_user(self):
        with allure.step("Login as user with email vinkotov@example.com"):
            data = {
                "email": "vinkotov@example.com",
                "password": "1234"
            }
            response1 = MyRequests.post("/user/login", data=data)
            print(response1.content)
        
        with allure.step("Extract auth_sid, token, and user_id from login response"):
            auth_sid = self.get_cookie(response1, "auth_sid")
            token = self.get_header(response1, "x-csrf-token")
            user_id_from_auth_method = self.get_json_value(response1, 'user_id')
        
        with allure.step("Attempt to get details of another user (user with ID 1)"):
            headers = {"x-csrf-token": token}
            cookies = {"auth_sid": auth_sid}
            response2 = MyRequests.get("/user/1", headers=headers, cookies=cookies)
            print(response2.content)
        
        with allure.step("Verify response contains 'username' and does not contain 'email', 'firstName', 'lastName'"):
            Assertions.assert_json_has_key(response2, "username")
            Assertions.assert_json_has_not_key(response2, "email")
            Assertions.assert_json_has_not_key(response2, "firstName")
            Assertions.assert_json_has_not_key(response2, "lastName")