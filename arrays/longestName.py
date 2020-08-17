if __name__ == '__main__':
    for _ in range(int(input())):
        biggest = ""
        for i in range(int(input())):
            n = input()
            if len(n) > len(biggest):
                biggest = n
        print(biggest)
