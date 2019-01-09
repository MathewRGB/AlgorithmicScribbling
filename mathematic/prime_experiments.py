import matplotlib.pyplot as plt
import math
import random


def check_for_prime(number):
    if number == 1 or number == 2 or number == 3:
        return True

    for num in range(2, int(math.sqrt(number) + 1)):
        if (number % num) == 0:
            return False

    return True


def check_for_prime_naiv(number):
    if number == 1 or number == 2 or number == 3:
        return True

    for num in range(2, int(number / 2)):
        if (number % num) == 0:
            return False

    return True


def get_prime_by_n(n):
    prime_counter = 2
    current_number = 1

    if (n == 1):
        return 1

    if (n == 2):
        return 2

    while (prime_counter != n):
        current_number += 2
        if check_for_prime(current_number):
            prime_counter += 1

    return current_number


def get_list_of_primes_by_count(number_of_primes):
    prime_list = []

    for n in range(1, number_of_primes):
        prime_list.append(get_prime_by_n(n))

    return prime_list


def calc_list_of_differences_from_list(number_list):
    if len(number_list) <= 1:
        return None

    diff_list = []
    prev_number = number_list[0]

    for i in range(1, len(number_list)):
        diff_list.append(number_list[i] - prev_number)
        prev_number = number_list[i]

    return diff_list


def calc_sumlist_each_by_element(number_list):
    if len(number_list) <= 1:
        return None

    sum_list = []
    prev_sum = number_list[0]

    for i in range(1, len(number_list)):
        sum_list.append(number_list[i] + prev_sum)
        prev_sum = sum_list[i - 1]

    return sum_list


def get_special_list(num_of_elems):
    special_list = []

    for i in range(num_of_elems):
        special_list.append(special_function_by_n(i))

    return special_list


def special_function_by_n(n):
    return int((n ** 1.001) * math.log(n + 1) + 1)


def pi(n):
    counter_list = []
    prime_counter = 0

    for i in range(1, n):
        counter_list.append(prime_counter)
        if check_for_prime(i):
            prime_counter += 1

    return counter_list


def Li(n):
    counter_list = []
    prev_number = 0

    for i in range(2, n):
        curr_number = prev_number + 1 / math.log(i)
        counter_list.append(curr_number)
        prev_number = curr_number

    return counter_list


def random_walk(n):
    counter_list = []
    counter_list.append(0)
    prev_number = 0

    for i in range(1, n):
        if random.getrandbits(1) == 1:
            counter_list.append(prev_number + 1)
            prev_number = prev_number + 1
        else:
            counter_list.append(prev_number - 1)
            prev_number = prev_number - 1

    return counter_list


# draw the figure so the animations will work
fig = plt.gcf()
fig.show()
fig.canvas.draw()

for i in range(1000):
    plt.step(range(10000), random_walk(10000))
    # update canvas immediately
    plt.xlim([0, 10000])
    plt.ylim([-250, 250])
    plt.pause(1)  # I ain't needed!!!
    fig.canvas.draw()
