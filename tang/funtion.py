'''DaysPerYear=365
HoursPerDay=24
MinutesPerHour=60
SecondsPerMinute=60
sum=int(DaysPerYear*HoursPerDay*MinutesPerHour*SecondsPerMinute)
print("一年是有多少秒?")
print(sum)

string = """我爱鱼C，
正如我爱小甲鱼，
他那呱唧呱唧的声音，
总缠绕于我的脑海，
久久不肯散去……
"""
print(string)'''

'''dict1 = dict((('a1',66),('b1',6688)))
print(dict1['a1'])

dict2 =dict(ab = 'hello world',bb = 'dd4434')
print(dict2['ab'])

dict2['ab'] = 'tan tan'
print(dict2['ab'])

dict2['ww'] = 'ban ban'
print(dict2)'''

'''dicta = {}
d = dicta.fromkeys(range(1,11),"赞")'''

'''for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i)'''

"""print(d.get(12,'num'))
for i in d.items():
    print(i)"""

a = {1:'one',2:'two',3:'three'}
b = a.copy()
c = a
print(id(a))
print(id(b))
print(id(c))
a.setdefault("小白")
b = {"小白":"猫"}
a.update(b)
print(a)