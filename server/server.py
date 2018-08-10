#!/usr/bin/python
# coding:utf-8

import web
import sys

# 脚本目录
SCRIPT_DIR = sys.path[0]
# 字典文件路径
DICT_FILE_PATH = SCRIPT_DIR + "/resource/dict.txt"

# 请求接口和实际处理类的对应关系
# 所有符合/translate/(.*)交给query类去处理
urls = (
    '/translate/(.*)', 'query'
)
# 创建服务器对象
app = web.application(urls, globals())


class query:
    def GET(self, origin_word):
        my_dict = load_dict()
        if not origin_word:
            return u"缺少参数"
        return my_dict.get(origin_word, u"没有找到")


def xread_file_lines(file_name):
    '''
    逐行读取文件
    '''
    file = open(file_name, 'r')
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            line = line.rstrip('\n')
            yield line
    file.close()


def load_dict():
    """
    加载字典文件
    :return: dict
    """
    d = dict()
    for line in xread_file_lines(DICT_FILE_PATH):
        # 源文件的内容是用逗号分隔的两列，第一列是英文，第二列是中文
        arr = line.split(",")
        origin_word = arr[0]
        target_word = arr[1]
        #  设置字典，键是英文，值是中文
        d[origin_word] = target_word
    return d


if __name__ == "__main__":
    # 启动服务器
    app.run()
