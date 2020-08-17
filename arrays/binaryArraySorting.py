# Problem: https://practice.geeksforgeeks.org/problems/binary-array-sorting5355/1

#User function Template for python3

'''
arr: List of integers denoting the input array
n  : size of the given array

You need to return the sorted binary array
'''
def sortBinaryArray (arr, n):
    arr.sort()
    return arr


import math

def main():
    T = int(input())
    while T > 0:
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        res = sortBinaryArray(arr, n)
        for i in range(n):
            print(res[i], end=" ")

        print("")
        T -= 1


if __name__ == '__main__':
    main()