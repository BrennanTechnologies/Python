import random


# lst = []
# for i in range(1,100):
# 	i = random.randint(0,9)
# 	lst.append(i)
# 	print(i)
# print(lst)


# Dice Roller:
# --------------------------------------------
lst = []
def dice_roller():
	for i in range(0,9):
		roll = random.randint(0,9)
	return roll
#results = dice_roller()
#print(results)

# Fill out Ticket: (10x)
# --------------------------------------------
len_of_ticket = 10

def buy_ticket():
	ticket = []
	for i in range(0,len_of_ticket):
		i = dice_roller()
		ticket.append(i)
	return ticket
#myTicket = buy_ticket()
#print(myTicket)


# Buy 100 Tickets
# --------------------------------------------
all_tickets = []
for i in range(0,100):
	myTicket = buy_ticket()
	all_tickets.append(myTicket)
	print("prrrttt!... " + str(myTicket))


for ticket in all_tickets:
	while True:
		if 


	print(ticket)
	for i in ticket:
		print(i, end=',')

	


#print(ticket for ticket in all_tickets)




# Secure module
# The cryptographically secure random generator generates random data using synchronization methods to ensure that no two processes can obtain the same data simultaneously.
# https://pynative.com/python-secrets-module/#h-why-use-the-secrets-module


# Random
# https://github.com/python/cpython/blob/3.10/Lib/random.py
	
# Are two tickets Unique?
# --------------------------------------------
	





# lst = []
# def dice_roller():
# 	for i in range(0,9):
# 		lst.append(random.randint(0,9))
# 	print(lst)

# results = dice_roller()
# print(results)



# i = 0
# while i!=100:
# 	i  = i + 1
# 	print(i)
	
	
	#rnd = i
	#rnd = random.randint(0,9)
	#print(rnd)


#ticket_no = []
#ticket_len = range(0,9)

#i for range(0,9):
#	print(ticket_len)


# for in range:
# 	random.randint(0,9)
# 	ticket_no.append(rnd)