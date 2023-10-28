random_list = [
    105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"
]

def units(x) :
    units = x % 10
    tens = (x // 10) % 10
    hundreds = (x // 100) % 10
    return {"units": units, "tens": tens, "hundreds": hundreds}

integers_parts = list(filter(lambda x : isinstance(x, int),random_list))
float_parts = tuple(filter(lambda x : isinstance(x, float),random_list))
string_parts = list(filter(lambda x : isinstance(x, str),random_list))
    
integers = list(map(units,integers_parts))

print(f"Data float : {float_parts}")
print(f"Data int :")
for x in integers:
    print(x)
print(f"Data string : {string_parts}")