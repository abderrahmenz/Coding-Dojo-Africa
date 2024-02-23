def countdown(num):
    return list(range(num, -1, -1))

def print_and_return(lst):
    print(lst[0])
    return lst[1]

def first_plus_length(lst):
    return lst[0] + len(lst)

def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    second_value = lst[1]
    new_lst = [val for val in lst if val > second_value]
    print(len(new_lst))
    return new_lst

def length_and_value(size, value):
    return [value] * size

print(countdown(5))
print(print_and_return([1, 2]))
print(first_plus_length([1, 2, 3, 4, 5]))
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))
print(length_and_value(4, 7)) 
print(length_and_value(6, 2)) 
