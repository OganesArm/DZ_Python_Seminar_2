#Реализуйте алгоритм перемешивания списка.
import random

def new_list(size: int) -> list:
    list_ = []
    for i in range(size):
        list_.append(i)
    return list_


my_list = new_list(10)

def my_shuffle(my_list: list):
    for i in range(len(my_list)):
        ni = random.randint(0, len(my_list)-1)
        my_list.append(my_list.pop(ni))   # Выдергиваем число по рандомному индексу

print(my_list)
my_shuffle(my_list)
print(my_list)




"""import random

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
print(f"Новый список: {mixed_list}")"""
