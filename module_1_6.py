my_dict = {'Nikita': 1998, 'Natalya': 1998}
print(my_dict)
print(my_dict['Nikita'])
print(my_dict.get('Anton'))
my_dict.update({'Kira': 2024, 'Mia': 2021})
print(my_dict)
del my_dict['Nikita']
print(my_dict)

my_set = {1, 2, 3, 1, 2, 3, 'Nikita', True, (1, 2, 3)}
print(my_set)
print(my_set.add(4))
print(my_set)
print(my_set.discard(1))
print(my_set)