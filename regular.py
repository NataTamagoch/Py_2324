import re
stroka = 'Privet, meny sovut Kirill, mne 38 let, moi telefon 8974123698 , moi index 12345678, a pochta kmmmorozov@gmail.com, rabochiy telefon - 23456789'

result = re.match(r'Pri',stroka)
print(result)
print(result.group(0))
print(result.start())
print(result.end())
################################
result = re.search(r'telefon',stroka)
print(result)

result = re.split(r'moi',stroka)
print(result)

result = re.findall(r'telefon',stroka)
print(result)

import requests
import re

result = requests.get('https://ipap.ru')
text = result.text
phones = re.findall(r'\b\d\d\d\d\d\d\d\b|\b\d\d\d\d\d\d\d\d\d\d\d\b', text)
print(phones)
emails = re.findall(r'\w+@\w+.\w+',text)
print(emails)
