# a = {'name': "tangky", "age": 27, "sex": 1}
# b = a.setdefault('name', 1)
# print(a)
# print(b)
# set
my_list = ['a', 'a', 'b', 'a', 'b', 'c']
my_dict = {key: my_list.count(key) for key in my_list}
# for i in my_list:
#     if i not in my_dict.keys():
#         my_dict[i] = 1
#     else:
#         my_dict[i] += 1

print(my_dict)