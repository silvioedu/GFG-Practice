# Problem: https://practice.geeksforgeeks.org/problems/kth-smallest-element/0

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        position = int(input())
        arr.sort()
        print(arr[position-1])