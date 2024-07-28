import pytest
from base.base_case import BaseCase
from base.assertions import Assertions
from base.my_requests import MyRequests
import allure


@allure.epic("Authorization cases")
@allure.feature("User Authorization")
class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup_method(self):
        with allure.step("Setup: User login"):
            data = {
                'email': 'vinkotov@example.com',
                'password': '1234'
            }
            response1 = MyRequests.post("/user/login", data=data)
            self.auth_sid = self.get_cookie(response1, "auth_sid")
            self.token = self.get_header(response1, "x-csrf-token")
            self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    @allure.description("This test successfully authorizes a user by email")
    @allure.story("Positive Authorization")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auth_user(self):
        with allure.step("Check user authentication status"):
            response2 = MyRequests.get(
                "/user/auth",
                headers={"x-csrf-token": self.token},
                cookies={"auth_sid": self.auth_sid}
            )

        with allure.step("Verify user id matches"):
            Assertions.assert_json_value_by_name(
                response2,
                "user_id",
                self.user_id_from_auth_method,
                "User id from auth method is not equal to user id from check method"
            )

    @allure.description("This test checks auth status without sending auth cookies or token")
    @allure.story("Negative Authorization")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        with allure.step(f"Attempt to authenticate without {condition}"):
            if condition == "no_cookie":
                response2 = MyRequests.get(
                    "/user/auth",
                    headers={"x-csrf-token": self.token}
                )
            else:
                response2 = MyRequests.get(
                    "/user/auth",
                    cookies={"auth_sid": self.auth_sid}
                )

        with allure.step("Verify user is not authenticated"):
            Assertions.assert_json_value_by_name(
                response2,
                "user_id",
                0,
                f"User is authorized with condition {condition}"
            )