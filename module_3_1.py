calls = 0


def count_calls(calls):
    return calls


def string_info(string):
    global calls
    calls += 1
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    global calls
    calls += 1
    a = True
    b = string.lower()
    for i in range(0, len(list_to_search)):
        c = (list_to_search[i])
        c = c.lower()
        if b == c:
            a = True
            break
        else:
            a = False

    return a


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
