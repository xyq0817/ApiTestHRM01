import unittest
from api.emp_api import EmpApi
import logging
from utils import assert_common, get_emp_data, get_emp_dataq, get_emp_datam, get_emp_datad, DBUtils
import app
from parameterized import parameterized


class TestHRMEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = EmpApi()

    @classmethod
    def tearDownClass(cls) -> None:
        ...

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    @parameterized.expand(get_emp_data)
    def test01_add_emp(self, username, mobile, success, code, message, http_code):
        response = self.emp_api.add_emp(username, mobile)
        jsonData = response.json()
        logging.info("添加员工返回数据为{}".format(jsonData))
        assert_common(self, response, http_code, success, code, message)
        app.EMP_ID = jsonData.get("data").get("id")

    @parameterized.expand(get_emp_dataq)
    def test02_query_emp(self, success, code, message, http_code):
        response = self.emp_api.query_emp()
        logging.info("查询员工返回的数据{}".format(response.json()))
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(get_emp_datam)
    def test03_modify_emp(self, username, success, code, message, http_code):
        response = self.emp_api.modify_emp(username)
        data = response.json()
        logging.info("修改员工返回的数据{}".format(data))
        with DBUtils() as db_utils:
            sql = "select username from bs_user where id={}".format(app.EMP_ID)
            db_utils.execute(sql)
            result = db_utils.fetchone(sql)[0]
            logging.info("数据库中数据为：{}".format(result))
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(get_emp_datad)
    def test04_delete_emp(self, success, code, message, http_code):
        response = self.emp_api.delete_emp()
        logging.info("删除员工返回的数据{}".format(response.json()))
        assert_common(self, response, http_code, success, code, message)
