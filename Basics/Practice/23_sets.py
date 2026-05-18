def solution():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    fronzenset1 = frozenset(set1)
    fronzenset2 = frozenset(set2)
    diff = fronzenset1.difference(fronzenset2)
    return diff

def main():
    print(solution())

if __name__ == '__main__':
    main()