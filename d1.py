d1 = {'kirill':'897456321', 'ivan':'78663214', 'pavel':'445699663'}

d2 = {
    'feder':'54645663',
    'stepan':'45979864',
    'nikalay':'45487888',
    'kirill':'111111111'
}

d1.update(d2)
print(d1)
d1['savely'] = '7888522'
print(d1)

#print(d1['kirill'])
#print.(d1.items())
#print(d1.keys())
#print(d1.values())



name = input('Введите имя:')
name = name.lower() #написать строчными
print(name)
print(f'Телефон абонента {name} - {d1.get(name, "не найден")}')



