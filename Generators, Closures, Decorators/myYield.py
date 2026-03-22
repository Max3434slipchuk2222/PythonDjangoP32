def get_numbers():
    return [1, 2, 3]


print("get_numbers() - default", get_numbers())


def get_yield_numbers():
    yield 1
    yield 2
    yield 3


# print("get_yield_numbers()", get_yield_numbers())
print("---get_yield_numbers()---")
for item in get_yield_numbers():
    print(item, end="\t")

print()


def my_counter_yield(n):
    i = 1
    while i <= n:
        yield i
        i += 2


for item in my_counter_yield(7):
    print(item, end='\t')
