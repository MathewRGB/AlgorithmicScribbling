import math
import argparse

from mathematic.prime_experiments import is_prime, get_prime_by_n



def get_int_array(string):
    if not isinstance(string, str):
        raise TypeError("parameter string is not of type str.")

    result = bytearray()
    result.extend(map(ord, string))

    return result


def get_min_max_range(min_int, max_int):
    if max_int <= min_int:
        raise ValueError("max_int has to be bigger than min_int.")

    return max_int - min_int + 1


def get_prime_hash(password, target_length, min_byte, max_byte):
    i_array = get_int_array(password)

    i_min_byte = int(min_byte)
    i_max_byte = int(max_byte)
    modul = get_prime_by_n(target_length)
    min_max_range = get_min_max_range(i_min_byte, i_max_byte)

    new_password = None

    for i in range(target_length):
        new_int = (i_array[i % len(i_array)] + modul + get_prime_by_n(
            (i + sum(i_array)) + i_array[(i + sum(i_array)) % len(i_array)])) % min_max_range + i_min_byte

        if not new_password:
            new_password = chr(new_int)
        else:
            new_password += chr(new_int)

    return new_password


def main():
    parser = argparse.ArgumentParser(description='Prime hash calculator')

    parser.add_argument('-p', dest="password", type=str, default=False)
    parser.add_argument('-t', dest="target_length", type=int)

    parsed_args = parser.parse_args()

    calculated_hash = get_prime_hash(parsed_args.password, parsed_args.target_length, min_byte=33, max_byte=126)

    print(f"Calculated hash out of the given string \"{parsed_args.password}\"  is: {calculated_hash}")
  
if __name__== "__main__":
  main()
