import json
from json.decoder import JSONDecodeError
import requests
import pytest
class TestUserAgent:

    heads=[
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Mobile", "No", "Android"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1","Mobile","Chrome", "iOS"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)","Googlebot", "Unknown", "Unknown"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0","Web", "Chrome", "No"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1","Mobile", "No", "iPhone")
    ]

    @pytest.mark.parametrize('headers1, expected1, expected2,expected3',heads)

    def test_user_agent(self,headers1, expected1, expected2,expected3):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        response1 = requests.get(url, headers = {"User-Agent":headers1})
        response_dict = response1.json()
        assert response_dict['platform'] == expected1, f"Поле  platform некорректно, выходит {response_dict['platform']}, ожидаемо: {expected1}"
        assert response_dict['browser'] == expected2, f"Поле  browser некорректно, выходит {response_dict['browser']}, ожидаемо: {expected2}"
        assert response_dict['device'] == expected3, f"Поле  device некорректно, выходит {response_dict['device']}, ожидаемо: {expected3}"