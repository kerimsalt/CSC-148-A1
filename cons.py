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
