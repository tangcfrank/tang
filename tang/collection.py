print("-------------------------collection（集合）----------------------------")
n = {1,2,3,4,5}
print(n)
print(type(n))

a = set([1,2,3,4,5])
print(set(a))
print(type(a))
print(type(n))

for i in a:
    print(i)
print(1 in a)

b = {56,7,8,99}
b.add(88)
print(b)

n.add(99)

c = {22,2,2,344,55,66,1,2,3,4,5,6}
print(c)

d = frozenset([1,2,3,4,5,6])
