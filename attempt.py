import pymysql

connection = pymysql.connect(host="nadejnei.net", user="student", password="1q2w#E$R", database="test", port=33306)
cursor = connection.cursor()
cursor.execute('select * from telsprav')
data = cursor.fetchall()

for elem in data:
    print(elem)
   phone = elem[0]
   sex = elem[1]
   surname = elem[2]
   name = elem[3]

telspav = ({phone}, {sex}, {surname}, {name})
f = open('users2.txt','w')

for elem in data:
    f.write(telsptav+';')

f.close()