import unittest
from script.test_login import TestHRMLogin
import time
import app
from tools.HTMLTestRunner import HTMLTestRunner
from script.login import Login
from script.test_emp import TestHRMEmp

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(TestHRMEmp))
# suite.addTest(unittest.makeSuite(TestHRMLogin))
report_path = app.BASE_DIR + "/report/ihrm{}.html".format(time.strftime("%Y%m%d %H%M%S"))
with open(report_path, mode="wb") as f:
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力资源接口测试", description="v1.1")
    runner.run(suite)
