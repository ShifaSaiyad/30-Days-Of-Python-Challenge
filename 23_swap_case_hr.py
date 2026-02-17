def swap_case(s):
    s_n = s.swapcase()
    return s_n

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)