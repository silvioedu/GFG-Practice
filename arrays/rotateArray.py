# Problem: https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0

if __name__ == '__main__':
    for _ in range(int(input())):
        n, d = map(int, input().split())
        arr = list(map(int, input().split()))
        arr = arr[d:] + arr[:d]
        [print(arr[i], end=" ") for i in range(n)]
        print()
