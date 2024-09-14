def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
values_list = [2, 'Anka', False]
values_dict = {'a':3, 'b':4,'c': 5}
values_list_2 = [5.1, 'Anka']
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)

#def append_to_list(item, my_list=None):
 #   if my_list is None:
  #      my_list=[]
  #      my_list.append(item)
  #  print(my_list)
#append_to_list(5)