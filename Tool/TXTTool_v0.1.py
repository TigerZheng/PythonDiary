"""
    Author：Tiger Z
    Time  ：2020-4-20 11:01:56
    Log   ：
        v0.1：
            通过with语句操作txt文档，同时优化信息读取策略
            每次读取1行，然后进行处理，节约程序运行开销
"""


if __name__ == "__main__":

    # 打开文档
    file1 = open("test.txt", "w")
    # 写数据
    file1.write("Hello  World!!")
    # 读数据
    file1 = open("test.txt", "r")
    data = file1.read()
    print(data)
    # 记住文件处理完，关闭是个好习惯
    file1.close()

    fw = open("/exercise1/data/query_deal.txt", 'w')  # 将要输出保存的文件地址
    for line in open("/exercise1/data/query.txt"):  # 读取的文件
        fw.write("\"poiName\":\"" + line.rstrip("\n") + "\"")  # 将字符串写入文件中
        # line.rstrip("\n")为去除行尾换行符
        fw.write("\n")  # 换行
fw.close()

# 若文件不存在，系统自动创建。'a'表示可连续写入到文件，保留原内容，在原内容之后写入。可修改该模式（'w+','w','wb'等）
f = open("data/model_Weight.txt", 'a')
f.write("hello,sha")  # 将字符串写入文件中
f.write("\n")  # 换行  
f.close()

with open(rb"test.txt") as f:
