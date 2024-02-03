l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

oddelem = l1[1::2]
evenelem = l2[0::2]
print(oddelem)
print(evenelem)

odd = []
for i in l1:
	if i % 2 != 0:
		odd.append(i)

even = []
for i in l2:
	if i % 2 == 0:
		even.append(i)



print(odd)
print(even)

l3 = odd + even
print(l3)

