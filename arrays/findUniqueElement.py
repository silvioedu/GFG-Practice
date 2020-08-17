# Problem: https://practice.geeksforgeeks.org/problems/find-unique-element/0
from collections import Counter

if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        numbers = list(map(int, input().split()))
        count = Counter(numbers)
        for number, qty in zip(count.keys(), count.values()):
            if qty == 1:
                print(number)
