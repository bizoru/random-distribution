
import random
import math


def basic_list(size):
    return [1.0 / size for item in range(size)]


def check_list(a_list):
    return sum(a_list)


def entropy(distribution):
    result = 0.0
    for probability in distribution:
        result += probability * math.log(1.0 / abs(probability), 2)
    return result


def create_random_probability(size):
    b = basic_list(size)
    rn_increase = b[0]
    pending_balance = 0.0
    for index, value in enumerate(b):
        if (index + 1) % 2 != 0:
            random_sign = 1 if random.randint(-1, 1) > 0 else -1
            random_increase = random_sign * random.uniform(0, rn_increase)
            pending_balance = -1 * random_increase
            b[index] += random_increase
        else:
            b[index] += pending_balance
        if index + 1 == len(b) and (index + 1) % 2 != 0:
            b[0] += pending_balance
    return b


def simulate():
    for number in range(1, 1000, 1):
        distribution = create_random_probability(number)
        entropy_result = entropy(distribution)
        print "number: {} , entropy: {} ".format(number, entropy_result)


simulate()

