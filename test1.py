# 15. 元组：
# 不可变的序列元组的每一项可以是 数字 字符串 列表  元组
# 使用的（元素1，元素2，……）
tup=(1,2,3,4,5)
# # 获取元组下标长度  len(元组名)
print(len(tup))
# # 通过下标获取对应的元素  tup[下标]
print(tup[0])
# # 检测类型 使用： type()  返回的结果： tuple 元组
print(type(tup))
# # 判断元素是否在元组内  in  not in  返回的是布尔值 True  False
print(1 in tup)
print(1 not in tup)
# # 通过元素去查找元素所在元组的位置  tup.index(元素)
print(tup.index(2))
# # 判断元组内最大值  只适用于 纯数字   max(元组名)
print(max(tup))
# # 判断元组内最小值  只适用于 纯数字   min(元组名)
print(min(tup))
# # 统计一个元素在元组里出现的次数    tup.count(元素)
print(tup.count(1))
# # 把元组转为字符串 str(元组名)
print(type(str(tup)))
# 16字典： 键值对的组合   使用的{key1:value1,key2:value2，……}
# 键必须是唯一的 ，可以由 字符串 、数字、元组组成 但是不可以由列表 字典作为键
#
# 检测字典类型  type()
dict ={'name':'123','age':12,10:23}
print(type(dict))
# # 判断字典的键 是否在 字典内  使用  in  not in
print('name' in dict)
print('123' in dict)
dict1={'name':'qzx',(12,14):48,12:58}
# # dict.keys()   获取是所有的键
print(dict1.keys())
# # dict.values()  获取所有的键 对应的值
print(dict1.values())
# # dict.items()  获取的是所有的字典的每一个键值对 以列表的形式返回
# print(dict1.items())
# # dict.pop(key)  通过指定的键名 删除指定的键名对应的键值对
# print(dict1.pop('name'))
# print(dict1)
# # dict.update(字典) 比如 dict.update({'name':'czw'})  如果存在这个键 那么就是修改
# dict1.update({'12':'14'})
# print(dict1)
# # dict.update(字典) 比如 dict.update({'age':18})   如果没有这个键 就默认在最后添加
# dict1.update({'age':18})
# print(dict1)
# # dict.copy（）   复制或者拷贝 字典dict
# dict1.copy()
# print(dict1)
# # dict.clear()  清空字典里面的元素  但是字典本身不被删除
# dict1.clear()
# print(dict1)
# # del  dict   删除字典  本身被删除
# del dict1
# print(dict1)
#
#
#
#
# python
#
#
# 13．字符串内置的方法：
# 1.通过字符 查找对应的索引 ：  str.index(对应的字符)
# str =' asdfghhj'
# print(str[0])
# # 2.判断字符串以...开头 ： str.startswith('对应的字符') 返回的是布尔值
# print(str.startswith('a'))
# print(str.startswith('b'))
# # 3.判断字符串以...结尾 ： str.endswith('对应的字符') 返回的是布尔值
# print(str.endswith('j'))
# # 4.字符串替换 ：  str.replace(old,new,count) count表示替换的个数  不写默认替换所有的
# print(str.replace('a','b'))
# # 5.字符串转大写： str.upper()
# print(str.upper())
# # 6.字符串转小写： str.lower()
# print(str.lower())
# # 7.去除字符串首位空格： str.strip（）
# print(str.strip())
# # 8.字符串的切割： str.split(切割的形式)
# print(str.split('g'))
# # 9.截取指定字符串 str[start:end] 包前不包后
# print(str[2:5])
#
# 14．列表常用的方法
# li[index] 通过指定的下标查询对应的元素
# li = [12,1,13,134,34]
# print(li[1])
# # li.index(下标) 通过指定的元素查询对应的下标
# print(li.index(34))
# # li[start:end]  通过指定的下标查询对应的元素 包含start  不包含 end   包前不包后
# print(li[0:3])
# # li.append(n)  在列表末尾追加一项n
# li.append(44)
# print(li)
# # li.insert(n,m)  n 代表下标  m 代表需要插入的值   在下标为n的位置插入m
# li.insert(2,123)
# print(li)
# # li.pop()  删除列表的最后一项  返回的结果是删除的那一项
# li.pop()
# print(li)
# # li.remove(n) 删除指定一项 n
# li.remove(34)
# print(li)
# # li.reverse() 把列表 翻转
# li.reverse()
# print(li)
# # li.sort()  把列表进行升序排列  只是适用于列表的每项都是数字
# li.sort()
# print(li)
# # li.copy() 复制列表
# li.copy()
# print(li)
# # li.clear() 清空列表
# li.clear()
# print(li)
# # li.count(元素) 统计某个元素的个数
# li.count(1)
# print(li)
# # del li 删除列表
# del li

