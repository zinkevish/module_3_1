from functools import wraps

call_counter = 0

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global call_counter
        call_counter += 1
        result = func(*args, **kwargs)
        return result
    return wrapper

@count_calls
def string_info(string):
    count_calls = len(string)
    string_info = string.upper(), string.lower()
    print((count_calls, *string_info))

@count_calls
def is_contains(string, list_to_search):
    string_lower = string.lower()
    for i in list_to_search:
        if string_lower == i.lower():
            return True
    return False




string_info("КапиБАРА")
string_info('Armageddon')
is_contains_1 = is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains_2 = is_contains('cycle', ['recycling', 'cyclic'])
print(is_contains_1)
print(is_contains_2)
print(call_counter)
