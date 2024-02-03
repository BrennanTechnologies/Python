dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
#print(dict3)

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}\t: {value}")

my_function(**dict1)
#my_function(name="John", age=25, country="USA")