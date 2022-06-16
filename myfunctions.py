def simple_separator():
    print("*" * 10)

def long_separator(count):
    print("*" * count)

def separator(simbol, count):
    print(simbol * count)

def hello_world():
    print("**********")
    print()
    print("Hello World!")
    print()
    print("##########")

def hello_who(who='World'):
    print("**********")
    print()
    print("Hello", who, "!")
    print()
    print("##########")

def pow_many(power, *args):
    solution = sum(args)**power
    print(solution)

def print_key_val(**kwargs):
    for k, v in kwargs.items():
        print(k, "-->", v)


def f(x):
    numbers = []
    for i in x:
        if i < 10:
            numbers.append(i)
    return numbers

def my_filter(iterable, f):
    print(f(iterable))









