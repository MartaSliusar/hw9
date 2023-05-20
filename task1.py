def add_one(lst):
    result = []
    number = ''
    for el in lst:
        number += str(el)

    num = int(number) + 1

    for el in str(num):
        result.append(int(el))
    return result

lst = [9,9,9,9]
print(add_one(lst))
