import pymysql

import app
import json


def assert_common(self, response, http_code, success, code, message):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


def get_json_data():
    json_path = app.BASE_DIR + "/data/login_data.json"
    with open(json_path, "r", encoding="utf-8") as f:
        data_list = []
        json_data = json.load(f)
        for i in json_data:
            data_list.append((i.get("mobile"), i.get("password"), i.get("http_code"), i.get("success"), i.get("code"),
                              i.get("message")))
        print(data_list)
        return data_list


def get_emp_data():
    path = app.BASE_DIR + "/data/emp_data.json"
    with open(path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        result = []
        add_emp_data = json_data.get("add_emp")
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        http_code = add_emp_data.get("http_code")
        result.append((username, mobile, success, code, message, http_code))
    print("添加的员工数据：{}".format(result))
    return result


def get_emp_dataq():
    path = app.BASE_DIR + "/data/emp_data.json"
    with open(path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        result = []
        query_emp_data = json_data.get("query_emp")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        http_code = query_emp_data.get("http_code")
        result.append((success, code, message, http_code))
    print("查询的员工数据：{}".format(result))
    return result


def get_emp_datam():
    path = app.BASE_DIR + "/data/emp_data.json"
    with open(path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        result = []
        modify_emp_data = json_data.get("modify_emp")
        username = modify_emp_data.get("username")
        success = modify_emp_data.get("success")
        code = modify_emp_data.get("code")
        message = modify_emp_data.get("message")
        http_code = modify_emp_data.get("http_code")
        result.append((username, success, code, message, http_code))
    print("修改的员工数据：{}".format(result))
    return result


def get_emp_datad():
    path = app.BASE_DIR + "/data/emp_data.json"
    with open(path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        result = []
        delete_emp_data = json_data.get("delete_emp")
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        http_code = delete_emp_data.get("http_code")
        result.append((success, code, message, http_code))
    print("删除的员工数据：{}".format(result))
    return result


class DBUtils:

    def __init__(self, host="182.92.81.159", user="readuser", password="iHRM_user_2019", database="ihrm"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self):
        self.con = pymysql.connect(self.host, self.user, self.password, self.database)
        self.cursor = self.con.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()

        if self.con:
            self.con.close()


if __name__ == '__main__':
    get_json_data()
