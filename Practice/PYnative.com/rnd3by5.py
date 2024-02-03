# Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5

import random

#---------------------------------------------------
# lst = []
# while len(lst) < 3:
# 	r = random.randint(100,999)
# 	if r % 5 == 0:
# 		lst.append(r)
#print(lst)
#---------------------------------------------------
'''
def generate_random():
    while True:
        r = random.randint(100, 999)
        if r % 5 == 0:
            return r
lst = [generate_random() for _ in range(3)]
print(lst)
'''
#---------------------------------------------------

# lst = []
# for num in range(3):
#     lst.append(random.randrange(100, 999, 5))
# print(lst)

# for _ in range(3):
#     lst.append(random.randrange(100, 999, 5))
# print(lst)

lst = [random.randint(100, 999) for _ in range(3) if random.randint(100, 999) % 5 == 0]
print(lst)


#---------------------------------------------------
    
#for num in range(3):
#    print(random.randrange(100, 999, 5), end=', ')
    
#---------------------------------------------------
#lst = [random.randint(100, 999) for _ in range(3) if random.randint(100, 999) % 5 == 0]
#print(lst)