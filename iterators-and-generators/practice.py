def gen_numbers(n):
    if i == n:
        yield i
    else:
        yield from gen_numbers(n + 1)

for i in gen_numbers(5):
    print(i)