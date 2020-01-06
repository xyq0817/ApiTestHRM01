import unittest
from api.login_api import LoginApi
import logging
import utils
from parameterized import parameterized


class TestHRMLogin(unittest.TestCase):
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

    @parameterized.expand(utils.get_json_data())
    def test01_login(self, mobile, pwd, http_code, success, code, message):
        response = self.login_api.login(mobile, pwd)
        json_data = response.json()
        logging.info("登陆测试返回的数据为{}".format(json_data))
        utils.assert_common(self, response, http_code, success, code, message)

    # def test02_username_is_not_exist(self):
    #     response = self.login_api.login("13900000002", "123456")
    #     json_data = response.json()
    #     logging.info("账号不存在返回的数据为{}".format(json_data))
    #     utils.assert_common(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # def test03_password_mistake(self):
    #     response = self.login_api.login("13800000002", "error")
    #     json_data = response.json()
    #     logging.info("密码错误返回的数据为{}".format(json_data))
    #     utils.assert_common(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # def test04_username_spacial_char(self):
    #     response = self.login_api.login("1380#@0002", "123456")
    #     json_data = response.json()
    #     logging.info("账号存在特殊字符返回的数据为{}".format(json_data))
    #     utils.assert_common(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # def test05_username_isnull(self):
    #     response = self.login_api.login("", "error")
    #     json_data = response.json()
    #     logging.info("账号为空返回的数据为{}".format(json_data))
    #     utils.assert_common(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # def test06_password_isnull(self):
    #     response = self.login_api.login("13800000002", "")
    #     json_data = response.json()
    #     logging.info("密码为空返回的数据为{}".format(json_data))
    #     utils.assert_common(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # def test07_username_have_chinese(self):
    #     response = self.login_api.login("1380000给奥02", "123456")
    #     json_data = response.json()
    #     logging.info("账号存在中文返回的数据为{}".format(json_data))
    #     utils.assert_common(self, response, 200, False, 20001, "用户名或密码错误")
    #
    # def test08_username_have_empty(self):
    #     response = self.login_api.login("1380000 02", "123456")
    #     json_data = response.json()
    #     logging.info("账号存在空格返回的数据为{}".format(json_data))
    #     utils.assert_common(self, response, 200, False, 20001, "用户名或密码错误")
