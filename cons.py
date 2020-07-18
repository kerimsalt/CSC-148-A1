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
