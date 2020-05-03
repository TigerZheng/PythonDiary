"""
    author ：Tiger Z
    Time   ：2020-4-19 15:00:13
    Comment：
        字典是一种可变容器模型，且可存储任意类型对象。
        字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中
        键一般是唯一的，如果重复,最后的一个键值对会替换前面的，值不需要唯一。
        值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
        字典键的特性
            字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。

        两个重要的点需要记住：
            1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，
            2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，
"""

if __name__ == '__main__':
    dict = {'a': 1, 'b': 2, 'b': '3'}

    # get(key, default)函数返回指定键的值，如果值不在字典中返回默认值
    print(dict.get('a', 0))
    print(dict.get('c', None))
    print(dict.get('d', 0))

    # fromkeys(seq, value)函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值
    seq = ('Google', 'Runoob', 'Taobao')
    dict1 = dict.fromkeys(seq)
    print("新字典为 : %s" % str(dict1))
    dict2 = dict.fromkeys(seq, 10)
    print("新字典为 : %s" % str(dict2))

    # 键一般是唯一的，如果重复,最后的一个键值对会替换前面的，值不需要唯一
    print(dict['b'])

    # 访问字典里的值
    print(dict['a'])
    # print(dict['z'])  #访问没有的键会报错

    # 向字典添加新内容的方法是增加新的键 / 值对，
    dict['z'] = "new"  # 添加
    print(dict['z'])

    dict['z'] = "old"  # 修改
    print(dict['z'])

    # 修改或删除已有键 / 值对
    print(dict)
    del dict['z']  # 删除键是'Name'的条目
    print(dict)

    # 清空字典所有条目
    dict.clear()
    print(dict)

    # 删除字典,删除后字典不存在
    del dict
    print(dict)
