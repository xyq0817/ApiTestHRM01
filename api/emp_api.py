import app
import requests


class EmpApi:
    def __init__(self):
        self.emp_url = app.Host + "/api/sys/user"
        self.headers = app.HEADERS

    def add_emp(self, username, mobile):
        data = {"correctionTime": "2020-01-07T16:00:00.000Z",
                "departmentId": "1210411411066695680",
                "departmentName": "测试",
                "formOfEmployment": 1,
                "mobile": mobile,
                "timeOfEntry": "2020-01-01",
                "username": username,
                "workNumber": "112"}
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        return response

    def query_emp(self):
        url = self.emp_url + "/" + app.EMP_ID
        return requests.get(url, headers=app.HEADERS)

    def modify_emp(self, username):
        url = self.emp_url + "/" + app.EMP_ID
        data = {"username": username}
        return requests.put(url, json=data, headers=self.headers)

    def delete_emp(self):
        url = self.emp_url + "/" + app.EMP_ID
        return requests.delete(url, headers=self.headers)
