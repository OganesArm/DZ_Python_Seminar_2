import random

def new_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list
    
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = new_list(list)

print(f"Оригинал:   {list}")
print(f"Новый список: {mixed_list}")