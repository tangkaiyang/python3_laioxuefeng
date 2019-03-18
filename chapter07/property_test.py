# -*- coding:UTF-8 -*-

# class Student():
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError("score must be an integer!")
#         if value < 0 or value > 100:
#             raise ValueError("score must between 0~100!")
#         self._score = value
#
#
# s = Student()
# s.score = 60
# print(s.score)
# s.score = 9999
#
#
# class Person():
#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#     @property
#     def age(self):
#         return 2015 - self._birth # age只读属性

"""
利用@property给Screen对象加上width和height属性,以及一个只读属性resolution
"""
class Screen():
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height



s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')