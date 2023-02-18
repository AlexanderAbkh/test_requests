import requests
import json

class BaseApi:
    def __init__(self, session):
        self.session = session
        self.request = requests

    def to_get(self, endpoint):

        return self.request.get(endpoint)

    def to_post(self, endpoint):

        return self.request.post(endpoint)

    def get_parsed_json(self, *args, **kwargs):

        resp = self.request.get(*args, **kwargs)
        return resp.json()

    def post_parsed_json(self, *args, **kwargs):

        resp = self.request.post(*args, **kwargs)
        return resp.json()

    def delete_parsed_json(self, *args, **kwargs):
        resp = self.request.delete(*args, **kwargs)
        return resp.json()

    def get_parsed_status_code(self, endpoint):
        """
        Парсим ответ со статус кодом
        :param endpoint: эндпоинт, где необходимо спарсить ответ
        :return: возвращает переменную со статус кодом
        """
        resp = self.request.get(endpoint)
        return resp.status_code

    @staticmethod
    def assertion_equal(actual, expected):
        """
        Метод упрощает сравнение результатов

        :param actual: актуальный результат
        :param expected: ожидаемый результат
        :return: Сравниваем актуальный с ожидаемым
        """
        assert actual == expected, f'we expected {expected} but got {actual}'


