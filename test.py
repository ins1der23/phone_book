with open ('phones.txt', 'r', encoding='UTF-8') as file:
    data = file.readlines()

with open ('test.txt', 'r', encoding='UTF-8') as file:
    data1 = file.readlines()

print('True') if data == data1 else print('False')

if data == data1: print("True") 
else: print('False') 