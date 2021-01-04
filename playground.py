import math


def fib(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n-2)

print(f"fib: {fib(10)}")
print(f"fib: {[x+1 for x in range(10)]}")


input = [3, 0, 1, 5, 4, 3, 2, 6, 4, 2, 3, 3, 0, 7, 1, 1, 2, 3, 4, 6]
# input = [fib(x + 1) for x in range(9)]


def mean(x):
    return sum(x) / len(x)


def quartile(vector, percentage):
    quartile = percentage * len(vector)
    vector.sort()
    return (mean([vector[math.floor(quartile) - 1], vector[math.floor(quartile)]])
            if math.floor(quartile) == quartile
            else vector[int(quartile)])


print(f"quartile(y, 0.25: {quartile(input, 0.25)}")
print(f"quartile(y, 0.5): {quartile(input, 0.5)}")
print(f"quartile(y, 0.75): {quartile(input, 0.75)}")


def mean_deviation(v):
    sigma = [abs(x - mean(v)) for x in v]
    return mean(sigma)


print(f"mean_deviation(input): {mean_deviation(input)}")
