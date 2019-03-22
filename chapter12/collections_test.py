#  -*-coding:UTF-8-*-

# from collections import namedtuple
#
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x)
# print(p.y)
# print(isinstance(p, tuple))
# print(isinstance(p, Point))

from collections import defaultdict

dd = defaultdict(lambda : 'N/A')
print(dd.items())
print(dd == {})