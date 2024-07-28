import requests
from base.base_case import BaseCase
from base.assertions import Assertions
from base.my_requests import MyRequests
import allure

@allure.epic("User Management")
@allure.feature("User Deletion")
class TestUserDelete(BaseCase):

    @allure.story("Delete User with ID 2")
    @allure.description("This test tries to delete a user with ID 2 and expects a 400 error with a specific message.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_user_by_id_2(self):
        with allure.step("Login as user with ID 2"):
            data = {
                'email': 'vinkotov@example.com',
                'password': '1234'
            }
            response1 = MyRequests.post("/user/login", data=data)

            auth_sid = self.get_cookie(response1, "auth_sid")
            token = self.get_header(response1, "x-csrf-token")
            user_id = self.get_json_value(response1, "user_id")

        with allure.step("Attempt to delete user with ID 2"):
            response2 = MyRequests.delete(
                f"/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid}
            )

        with allure.step("Verify the response status code and error message"):
            Assertions.assert_code_status(response2, 400)
            assert response2.json()["error"] == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."

    @allure.story("Delete Newly Created User")
    @allure.description("This test registers a new user, deletes them, and verifies the user is deleted.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_newly_created_user(self):
        with allure.step("Register a new user"):
            register_data = self.prepare_registration_data()
            response1 = MyRequests.post("/user/", data=register_data)

            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")

            email = register_data['email']
            password = register_data['password']
            user_id = self.get_json_value(response1, "id")

        with allure.step("Login as the newly created user"):
            login_data = {
                'email': email,
                'password': password
            }
            response2 = MyRequests.post("/user/login", data=login_data)

            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step("Delete the newly created user"):
            response3 = MyRequests.delete(
                f"/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid}
            )

        with allure.step("Verify user deletion"):
            Assertions.assert_code_status(response3, 200)

        with allure.step("Attempt to get the deleted user's data"):
            response4 = MyRequests.get(
                f"/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid}
            )
            Assertions.assert_code_status(response4, 404)

            try:
                response_json = response4.json()
            except requests.exceptions.JSONDecodeError:
                assert response4.text == "User not found", f"Unexpected response content {response4.text}"

    @allure.story("Delete User as Another User")
    @allure.description("This test registers two users and attempts to delete the first user while logged in as the second user.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_user_as_another_user(self):
        with allure.step("Register user 1"):
            register_data1 = self.prepare_registration_data()
            response1 = MyRequests.post("/user/", data=register_data1)

            Assertions.assert_code_status(response1, 200)
            Assertions.assert_json_has_key(response1, "id")

            user_id1 = self.get_json_value(response1, "id")

        with allure.step("Register user 2"):
            register_data2 = self.prepare_registration_data()
            response2 = MyRequests.post("/user/", data=register_data2)

            Assertions.assert_code_status(response2, 200)
            Assertions.assert_json_has_key(response2, "id")

            email2 = register_data2['email']
            password2 = register_data2['password']

        with allure.step("Login as user 2"):
            login_data2 = {
                'email': email2,
                'password': password2
            }
            response3 = MyRequests.post("/user/login", data=login_data2)

            auth_sid2 = self.get_cookie(response3, "auth_sid")
            token2 = self.get_header(response3, "x-csrf-token")

        with allure.step("Attempt to delete user 1 while logged in as user 2"):
            response4 = MyRequests.delete(
                f"/user/{user_id1}",
                headers={"x-csrf-token": token2},
                cookies={"auth_sid": auth_sid2}
            )

        with allure.step("Verify the response status code and message"):
            Assertions.assert_code_status(response4, 400)