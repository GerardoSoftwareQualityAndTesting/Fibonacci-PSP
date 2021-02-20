def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]


def overwrite_file(filename, num_list):
    str_list = '\n'.join(str(line) for line in num_list)
    with open(filename, "w+") as f:
        f.writelines(str_list)


def user_input():
    while True:
        try:
            n = int(input("Index of fibonacci: "))
            if n < 1:
                print("Please input an integer >= 1")
            else:
                return n
        except ValueError:
            print("Please input an integer >= 1")
            pass


fib_nums = read_integers("Code/fibonacci_nums.txt")


def fibonacci(n):
    global fib_nums
    return fib_nums[n] + fib_nums[n-1]


if __name__ == "__main__":
    n = user_input()
    if n > len(fib_nums):
        for i in range(len(fib_nums) - 1, n):
            fib_nums.append(fibonacci(i))
        overwrite_file("Code/fibonacci_nums.txt", fib_nums)

    for i in range(0, n):
        print(str(fib_nums[i]) + " ")
