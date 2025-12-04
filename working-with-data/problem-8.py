# Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list.

def cumulative_sum(values):
    for i in range(1, len(values)):
        values[i] = values[i-1] + values[i]
    return values

print(cumulative_sum(['a', 'b', 'c', 'd']))