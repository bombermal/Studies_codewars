def count(string):
    # The function code should be here
    return { key: string.count(key) for key in string}

print(count('aba'))