import argparse

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

parser = argparse.ArgumentParser(description="Convert temperature between Celsius and Fahrenheit.")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-c", "--celsius", type=float, help="Temperature in Celsius is to be converted to Fahrenheit")
group.add_argument("-f", "--fahrenheit", type=float, help="Temperature in Fahrenheit is to be converted to Celsius")

args = parser.parse_args()

if args.celsius is not None:
    result = c_to_f(args.celsius)
    print(args.celsius,"C = ", result, "F")
elif args.fahrenheit is not None:
    result = f_to_c(args.fahrenheit)
    print(args.fahrenheit,"F = ",result,"C")

