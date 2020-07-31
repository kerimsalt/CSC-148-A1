import sys
k = 3.34343532
print(round(k, 2))
lst = None
# does break affect if statement
# No it doesn't
i = 0
j = 0

while i < 9:
    if divmod(i, 2) != 0:
        print(i)
        break
    print("inside the loop")
l1 = [1,2,3]
l2 = [[1,2,3], 3, 6]
print(l1 in l2)

l1 = [1,2,3]
s1 = '[1,2,3]'
print(str(l1) == s1)
d1 = {'a': 1, 'b': 2}
ls = d1.values()
print(ls)
print(type(ls))
print('a' in d1)

min1 = sys.maxsize * -1
print(min1)

print(divmod(3, 5)[1])
print(30 % 6)

lst14 = list(range(9))
print(lst14[7:14])

print(type(lst14[7:14]))

d1 = {'a': 'b', '1': 2, '2': 1, 'c': 4, 'd': 3, '12': 6}
d1.pop('2')
print(list(d1.values()))
i = 7
if i:
    print(True)
