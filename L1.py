l1 = ['kirill', 'ivan', 'pavel', 'sergey']
l2 = ['maria', 'anna', 'svetlana']
print(l1)

print(type(l1))

l1.append('sergey')
print(l1)
l1.append(l2)
print(l1)
print(l1[2])  #pavel
print(l1[4][1])    #anna
l1.insert(0, 'alexandr') #добавила александра
print(l1)
l1.remove('kirill') #уд кирилла
print(l1)
l1.pop(2)  #уд элемент по индексу
print(l1)
print(l1.index('sergey')) #номр сергея
print(l1.count("sergey"))  #сколько сергеев
