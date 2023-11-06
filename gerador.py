
def contador(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1


gen = contador(10)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

