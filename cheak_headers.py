import json
from json.decoder import JSONDecodeError
import requests
import pytest
class TestHeaders:
    def test_headers(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response1.headers)

        assert 'Date' in response1.headers, "There is not Date in the response"
        assert 'Content-Type' in response1.headers, "There is not Content-Type in the response"
        assert 'Content-Length' in response1.headers, "There is not Content-Length in the response"
        assert 'Content-Type' in response1.headers, "There is notContent-Type in the response"
        assert 'Connection' in response1.headers, "There is not Connection in the response"
        assert 'Keep-Alive' in response1.headers, "There is not Keep-Alive in the response"
        assert 'Server' in response1.headers, "There is not Server in the response"
        assert 'x-secret-homework-header' in response1.headers, "There is not x-secret-homework-header in the response"
        assert 'Cache-Control' in response1.headers, "There is not Cache-Control in the response"
        assert 'Expires' in response1.headers, "There is not Expires in the response"

