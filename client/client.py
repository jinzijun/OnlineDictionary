# coding:utf-8

# 控件基础包，导入这个包后，这个包下的所有函数可以直接调用
from Tkinter import *

# 顶层窗口
top = Tk()  # 创建顶层窗口
top.geometry('250x150')  # 初始化窗口大小
top.title("网络词典")

# 标签上的可变文字
txt = StringVar()
txt.set("大家好")

# 标签控件
# 创建标签
label = Label(top, font='Helvetica -12 bold', textvariable=txt)
# 填充到界面
label.pack(fill=Y, expand=1)


def query(ev=None):
    """
    处理查询请求
    """
    # 从输入框组件中获取输入的内容
    origin_word = entry.get()
    # 网络请求，查询对应的翻译
    target_word = get_word(origin_word)
    if target_word is None:
        # 如果报错了，返回默认内容
        target_word = "没有找到"
    # 将查询结果设置在标签的可变文字
    txt.set(target_word)


# 创建输入框组件
entry = Entry(top)
# 绑定输入框事件。当输入框中，按下Enter，执行query函数
entry.bind('<Return>', query)
# 位置从左向右排列
entry.pack(side=LEFT)

# 创建按钮组件
query_button = Button(top, text="查询", command=query)
query_button.pack(side=LEFT)


def get_word(orgin_word):
    """
    调用HTTP接口获取答案
    :param orgin_word: 源单词
    :return:  目标单词
    """
    # 导入HTTP请求需要的库
    import urllib
    # 构造请求链接
    url = "http://localhost:8080/translate/%s" % orgin_word
    try:
        # 执行请求，并读取返回值
        response = urllib.urlopen(url=url).read().decode("utf-8")
    except Exception as e:
        print("Exception={0},url={1}".format(str(e), url))
        return None
    return response


if __name__ == '__main__':
    # 运行这个GUI应用
    mainloop()
