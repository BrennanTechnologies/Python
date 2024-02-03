employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dict1 = dict.fromkeys(employees, defaults)
print(dict1)

print(dict1["Kelly"])