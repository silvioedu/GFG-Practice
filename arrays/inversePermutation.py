if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))

        new_arr = sorted(arr)
        for i in range(n):
            x = arr[i]-1
            new_arr[x] = i+1
        print(*new_arr)

