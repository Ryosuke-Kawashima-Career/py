def solution():
    integer = [0, 1, 2, 3, 4]
    binary = ["0", "1", "10", "11", "100"]
    binary_dict = {}
    for i in range(len(integer)):
        binary_dict[integer[i]] = binary[i]
    additive_inverse = [-i for i in integer]
    sq_set = {i * i for i in integer}
    return binary_dict, additive_inverse, sq_set

def main():
    print(solution())

if __name__ == '__main__':
    main()