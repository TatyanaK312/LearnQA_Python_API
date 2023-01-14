import json
from json.decoder import JSONDecodeError
import requests
import pytest
class TestCookies:
    def test_cookies(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response1.cookies)
        cookie_value = response1.cookies.get('HomeWork')
        print(f"Значение cookies {cookie_value}")
        assert "HomeWork" in response1.cookies, "There is not cookies in the response"