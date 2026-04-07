# Given a positive integer n, check whether it is a power of 2 or not.

def power_of_2(N):
    if N <= 1:
        return False
    if N & (N-1) == 0:
        return True
    return False


if __name__ == "__main__":
    for i in range(1, 20):
        print("{} is a power of 2: {}".format(i, power_of_2(i)))    