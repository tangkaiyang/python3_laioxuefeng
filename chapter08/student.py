"""
对Student类编写单元测试,结果发现测试不通过,请修改Student类,让测试通过
"""
# -*-coding:UTF-8 -*-


class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError

        elif self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'