import logging
import os
from logging import handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Host = "http://182.92.81.159"
HEADERS = {"Content-type": "application/json"}
EMP_ID = 0


def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 设置处理器
    sh = logging.StreamHandler()
    # 设置文件处理器
    filename = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename, when="M", interval=1, backupCount=7)
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 把格式化器添加到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)
