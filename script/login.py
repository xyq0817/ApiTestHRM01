import unittest
from api.login_api import LoginApi
import logging
import utils
import app
from parameterized import parameterized


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    def test_login(self):
        response = self.login_api.login("13800000002", "123456")
        json_data = response.json()
        logging.info("登陆成功返回的数据为{}".format(json_data))
        utils.assert_common(self, response, 200, True, 10000, "操作成功")
        token = json_data.get("data")
        app.HEADERS["Authorization"] = "Bearer " + token
        logging.info("令牌{}".format(app.HEADERS))
