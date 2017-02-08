def get_gcd(numbers):
    if len(numbers) > 2:
        return get_gcd([numbers[0], get_gcd(numbers[1:])])

    a = abs(numbers[0])
    b = abs(numbers[1])

    while not b == 0:
        a, b = b, a % b

    return a

def get_lcm(numbers):
    if len(numbers) > 2:
        return get_lcm([numbers[0], get_lcm(numbers[1:])])

    return abs(numbers[0] * numbers[1]) // get_gcd(numbers)

print(get_lcm(range(1, 21)))