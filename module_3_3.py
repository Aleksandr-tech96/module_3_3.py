def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 3)
print_params(a = [1, 2], b = "Hello", c = False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [5, 6, 7]
values_dict = {"a": 10, "b": "Ball", "c": bool}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["Sport", 5.5]
print_params(*values_list_2, 42)