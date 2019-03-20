# -*- coding:UTF-8 -*-


import json

# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }
#
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
#
# s = Student('Bob', 20, 88)
# # print(json.dumps(s, default=student2dict))
# # print(s.__dict__)
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str, object_hook=dict2student))

"""
对中文进行JSON序列化时,json.dumps()提供了一个ensure_ascii参数,观察该参数对结果的影响
"""
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)