calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    result = (len(string), string.upper(), string.lower())
    return result

def is_contains(string, list_to_search):
    count_calls()
    result = False
    string = string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
        if string.__eq__(list_to_search[i]):
            result = True
            break
    return result

print(string_info("Happy New Year"))
print(string_info("Happy"))
print(string_info("New Year"))
print(is_contains("HaPPy", ["Happy", "New", "Year"]))
print(is_contains("Hapy", ["Happy", "New", "Year"]))
print(calls)